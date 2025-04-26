from django.db import models

# Create your models here.
class GuestBook(models.Model):
    id = models.AutoField(primary_key = True)
    title = models.CharField(max_length = 30)
    guest = models.CharField(max_length = 20)
    content = models.TextField() #방명록 내용 (TextField() -> 글자 수 제한 없음)
    password = models.CharField(max_length = 4) #방명록 비밀번호 (4자리 비번으로 제한)
    created = models.DateTimeField(auto_now_add=True) #방명록 생성 시 날짜와 시간 저장

    def __str__(self):
        return f"{self.title} : {self.guest}"