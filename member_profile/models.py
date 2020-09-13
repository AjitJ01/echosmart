from django.db import models

class IdProof(models.Model):
    class Meta:
        db_table = "id_proof"
    id_type = models.CharField(max_length=70, blank=False, default='')
    description = models.CharField(max_length=200, blank=False, default='')
    image = models.ImageField(upload_to='images/id_proofs', blank=True)