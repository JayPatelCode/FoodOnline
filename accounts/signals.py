from django.dispatch import receiver
from django.db.models.signals import post_save,pre_save
from accounts.models import User, UserProfile

@receiver(post_save, sender=User)
def post_save_create_profile_reciever(sender, instance, created, **kwargs):
    print(created)
    if created:
        UserProfile.objects.create(user=instance)
        print("user profile is created")
    else:
        try:
            profile = UserProfile.objects.get(user=instance)
            profile.save()
        except:
            #create profile if it does not exist
            UserProfile.objects.create(user=instance)
        #     print("profile does not exist, but i created one")
        # print("user is updated")

@receiver(pre_save, sender=User)
def pre_save_user_created(sender, instance, **kwargs):
    pass
    # print(instance.username, "this user is being saved")