# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ConversionChart(models.Model):
    _name = 'conversion.chart'
    _description = 'Conversion Chart'

    gauge = fields.Float('Gauge', digits=(12,4))
    mil = fields.Float('Mil', digits=(12,4))
    micron = fields.Float('Micron', digits=(12,4))
    millimeter = fields.Float('Millimeter', digits=(12,4))
    inch = fields.Float('Inch', digits=(12,4))

    @api.onchange('gauge')
    @api.depends('gauge','mil','micron','millimeter','inch')
    def gauge_convertion(self):
        for record in self:
            record.mil = record.gauge * 0.01
            record.micron = record.gauge * 0.25
            record.millimeter = record.gauge * 0.00025
            record.inch = record.gauge * 0.00001
    
    @api.onchange('mil')
    @api.depends('gauge','mil','micron','millimeter','inch')
    def mil_conversion(self):
        for record in self:
            record.gauge = record.mil * 100
            record.micron = record.mil * 25
            record.millimeter = record.mil * 0.025
            record.inch = record.mil * 0.001

    @api.onchange('micron')
    @api.depends('gauge','mil','micron','millimeter','inch')
    def micron_conversion(self):
        for record in self:
            record.gauge = record.micron * 4
            record.mil = record.micron * 0.004
            record.millimeter = record.micron * 0.001
            record.inch = record.micron * 0.00004

    @api.onchange('inch')
    @api.depends('gauge','mil','micro','millimeter','inch')
    def inch_conversion(self):
        for record in self:
            record.gauge = record.inch * 100000
            record.mil = record.inch * 1000
            record.micron = record.inch * 25000
            record.millimeter = record.inch * 25


    @api.onchange('millimeter')
    @api.depends('gauge','mil','micron','millimeter','inch')
    def millimeter_conversion(self):
        for record in self:
            record.gauge = record.millimeter * 4000
            record.mil = record.millimeter * 40
            record.micron = record.millimeter * 1000
            record.inch = record.millimeter * 0.04
        