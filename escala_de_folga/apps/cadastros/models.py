from django.db import models
from django.utils.translation import gettext as _


class DiaDaSemana(models.IntegerChoices):
    SEGUNDA = 0, _('Segunda-feira')
    TERCA = 1, _('Terça-feira')
    QUARTA = 2, _('Quarta-feira')
    QUINTA = 3, _('Quinta-feira')
    SEXTA = 4, _('Sexta-feira')
    SABADO = 5, _('Sabado')
    DOMINGO = 6, _('Domingo')

class Medico(models.Model):
    """Model que representa um Medico cadastrado no sistema."""

    nome = models.CharField(_("Nome"), max_length=50)
    sobrenome = models.CharField(_("Sobrenome"), max_length=50)
    admissao = models.DateField(_("Data de admissão"), auto_now=False, auto_now_add=False)
    folga = models.IntegerField(_("Dia de folga"), choices=DiaDaSemana.choices)
    

    class Meta:
        """Meta definition for Medico."""

        verbose_name = 'Médico'
        verbose_name_plural = 'Médicos'

    def __str__(self):
        """Unicode representation of Medico."""
        return f'{self.nome} {self.sobrenome}'


class Posto(models.Model):
    """Model que representa um Posto de Trabalho cadastrado no sistema."""

    nome = models.CharField(_("Nome"), max_length=50)
    endereco = models.TextField(_("Endereço"))

    class Meta:
        """Meta definition for Posto."""

        verbose_name = 'Posto'
        verbose_name_plural = 'Postos'

    def __unicode__(self):
        """Unicode representation of Posto."""
        return self.nome

class Escala(models.Model):

    data = models.DateField(_("Dia"), auto_now=False, auto_now_add=False)
    medico = models.ForeignKey("Medico", verbose_name=_(""), on_delete=models.CASCADE)
    posto = models.ForeignKey("Posto", verbose_name=_(""), on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("escala")
        verbose_name_plural = _("escalas")

    def __str__(self):
        return self.data
