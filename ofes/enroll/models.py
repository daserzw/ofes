from django.db import models

# Create your models here.

class Organization(models.Model):
    name = models.CharField(max_length=512)
    uri = models.CharField(max_length=1024)

class Entity(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    entity_id = models.CharField(max_length=1024)
    signing_keys = TextField
    metadata_endpoint = models.CharField(max_length=1024)
    
    def __repr__(self):
        
        return entity_id

    
    def enrollment_info(self):
        e_i = {
            'entity_id': self.entity_id,
            'signing_keys': self.signing_keys,
            'metadata_endpoint': self.metadata_endipoint
        }

        return e_i
