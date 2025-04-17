
import logging
import threading

from django.contrib.auth.password_validation import validate_password
from django.db import transaction
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login
# from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import EmailMessage
from django.contrib import messages
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.views import View, generic

from accounts.forms import CustomUserCreationForm
from accounts.token_service import account_activation_token
from accounts.user_service import UserService

from django.contrib.auth import get_user_model

logger = logging.getLogger(__name__)

User = get_user_model()

class SignUpView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        form = CustomUserCreationForm()

        return render(request, "registration/signup.html", {"form": form})

    def post(self, request: HttpRequest) -> HttpResponse:
        form = CustomUserCreationForm(request.POST)

        if not form.is_valid():
            return render(request, "registration/signup.html", {"form": form})

        try:
            with transaction.atomic():
                user = form.save(commit=False)
                user.is_active = False
                user.save()

                current_site = get_current_site(request)
                mail_subject = "Activate your account."
                message = render_to_string(
                    "registration/emails/acc_active_email.html",
                    {
                        "user": user,
                        "domain": current_site.domain,
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        "token": account_activation_token.make_token(user),
                    },
                )
                email = EmailMessage(mail_subject, message, to=[user.email])
                email.content_subtype = "html"

                # send message in the main thread, user will wait until message will be sent
                # email.send()

                # send message in a separate thread to avoid blocking the main thread
                threading.Thread(target=email.send).start()
        except Exception as e:
            logging.error(f"Error sending email: {e}")

            return render(request, "registration/signup.html", {"form": form})

        return render(request, "registration/email_confirmation_sent.html")


class SignUpGenericView(generic.CreateView):
    model = User
    template_name = "registration/signup.html"
    form_class = CustomUserCreationForm

    @transaction.atomic
    def form_valid(self, form):
        try:
            site_url = get_current_site(self.request)
            domain = site_url.domain
            password = form.cleaned_data["password1"]

            UserService.create_user(
                **form.cleaned_data, password=password, domain=domain
            )
        except Exception as e:
            logging.error(f"Error sending email: {e}")

            return render(self.request, "registration/signup.html", {"form": form})

        return render(self.request, "registration/email_confirmation_sent.html")


class ActivateAccountView(View):
    def get(self, request, uidb64, token):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if user is not None and account_activation_token.check_token(user, token):
            user.is_active = True
            user.save()
            # login(request, user)
            messages.success(
                request,
                "Thank you for confirming your email. You can now login to your account.",
            )
            return redirect("accounts:login")
        else:
            return render(request, "registration/activation_invalid.html")

