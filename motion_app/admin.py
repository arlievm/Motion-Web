from django.contrib import admin

from .models import Services , Proect
from .models import Customer , Team
from .models import Instruments, Technologies , TechnologiesCategory , Feedback


admin.site.register(Services)

admin.site.register(Customer)

admin.site.register(Proect)

admin.site.register(Team)

admin.site.register(Instruments)

admin.site.register(Technologies)
admin.site.register(TechnologiesCategory)

admin.site.register(Feedback)