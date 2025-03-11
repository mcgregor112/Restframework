from django import forms

class AppointmentBookingForm(forms.Form):
    doctor_name = forms.CharField(max_length=100)
    appointment_date = forms.DateField()
    amount = forms.DecimalField(max_digits=10, decimal_places=2)
