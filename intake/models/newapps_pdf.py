from django.db import models
from django.utils import timezone
from intake.constants import PACIFIC_TIME
from intake.models.abstract_base_models import BaseModel
from django.core.files.uploadedfile import SimpleUploadedFile


class NewAppsPDF(BaseModel):
    # includes created, updated from BaseModel
    applications = models.ManyToManyField(
        'intake.Application',
        related_name='prebuilt_multiapp_pdfs')
    pdf = models.FileField(upload_to='prebuilt_newapps_pdfs/')
    organization = models.OneToOneField(
        'user_accounts.Organization', related_name='newapps_pdf',
        on_delete=models.PROTECT)

    def set_bytes(self, bytes_):
        if not bytes:
            self.pdf = None
        else:
            now_str = timezone.now().astimezone(
                PACIFIC_TIME).strftime('%Y-%m-%d_%H:%M')
            filename = '{}_newapps_{}.pdf'.format(
                self.organization.slug, now_str)
            self.pdf = SimpleUploadedFile(
                filename, bytes_, content_type='application/pdf')

    def __str__(self):
        status = 'Prebuilt' if self.pdf else 'Unbuilt'
        return str(
            '{status} NewAppsPDF for {apps_count} applications to {org_name}. '
            'Updated: {updated}').format(
                status=status,
                apps_count=self.applications.count(),
                org_name=self.organization.name,
                updated=self.updated.astimezone(
                    PACIFIC_TIME).strftime('%Y-%m-%d %H:%M %Z'))
