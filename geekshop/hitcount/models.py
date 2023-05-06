from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver, Signal

# Свой собственный сигнал
some_signal = Signal()



class HitCount(models.Model):
    path = models.CharField(max_length=512, primary_key=True)
    hits = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.path} ({self.hits})'

    # Перехват процесса saveю Можно здесь или в коде ниже через сигнал
    # Принципиальных отличий в обоих способах нет!!!
    def save(self, *args, **kwargs):
        print(self)

        # собственный сигнал
        some_signal.send(self)
        return super().save(*args, **kwargs)


# В сигнале можно сразу обернуть на несколько моделей
# @receiver(post_save, sender=HitCount_N)
@receiver(post_save, sender=HitCount)
def post_save_hit(sender, instance, *args, **kwqargs):
    print(instance)

# собственный сигнал
@receiver(some_signal)
def post_save_hit(sender, *args, **kwqargs):
    print(sender)
