from django import forms
from django.core.mail.message import EmailMessage
from .models import Usuario

class ContatoForm(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(label='E-mail', max_length=100, initial="coffeebreak@coffeebreak.com", disabled=True)
    assunto = forms.CharField(label='Assunto', max_length=120)
    mensagem = forms.CharField(label='Mensagem', widget=forms.Textarea())

    def send_mail(self):
        nome = self.cleaned_data['nome']
        email = "coffeebreak@coffeebreak.com"
        assunto = self.cleaned_data['assunto']
        mensagem = self.cleaned_data['mensagem']

        conteudo = f'Nome: {nome}\nE-mail: {email}\nAssunto: {assunto}\nMensagem: {mensagem}'

        mail = EmailMessage(
            subject='E-mail enviado pelo sistema coffeebreak',
            body=conteudo,
            from_email='contato@seudominio.com.br',
            to=['contato@seudominio.com.br'],
            headers={'Reply-To': email}
        )
        mail.send()

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nome', 'endereco', 'cpf']
        labels = {
            'nome': 'Nome',
            'endereco': 'Endereço',
            'cpf': 'CPF'
        }

    def save_user(self):
        usuario = Usuario(
            nome=self.cleaned_data['nome'],
            endereco=self.cleaned_data['endereco'],
            cpf=self.cleaned_data['cpf']
        )
        usuario.save()
        return usuario
