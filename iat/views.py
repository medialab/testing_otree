# -*- coding: utf-8 -*-
from __future__ import division

from otree.common import Currency as c, currency_range, safe_json

from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class IAT(Page):
    form_model = models.Player
    form_fields = ['iat_results']

    def before_next_page(self):
        print self.player.iat_results


page_sequence = [
	IAT
]
