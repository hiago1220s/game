#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.entityFactory import EntityFactory


class Level:
    def __init__(self, window, name, game_mode):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list = []

        self.entity_list.extend(EntityFactory.get_entity('Level1bg'))

    def run(self):
        while True:
            self.window.fill((0, 0, 0))  # limpa a tela

            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()

            pygame.display.flip()  # atualiza a tela uma vez
