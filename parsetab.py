
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'a_parenteses a_parenteses_paragraph abbreviation baseword baseword_error double_word f_parenteses initial_letter middle1_word middle1_word_error middle1_word_error_2 middle2_word middle2_word_error middle_error_word middle_word_5 no_hifen no_hifen_paragraph normalword paragraph portugueseTranslation portugueseTranslationError prefix_error_word prefix_word prefix_word_error prefix_word_error_2 suffix_error suffix_error_word suffix_wordDict : Alphsection DictDict : Alphsection : initial_letter translationstranslations : normalword traducao translations\n    translations : normalword traducao no_hifen traducao translations\n                 | normalword traducao abbreviation traducao translations\n    \n    translations : normalword traducao multipleTranslations translations\n    \n    translations : baseword traducao multipleTranslations translations\n                 | baseword_error traducao multipleTranslations translations\n                 | baseword_error multipleTranslations translations\n    \n    translations : a_parenteses traducao f_parenteses traducao translations\n                 | a_parenteses_paragraph f_parenteses traducao translations\n    \n    translations : a_parenteses traducao baseword_error translations\n    translations : \n    multipleTranslations : middle2_word_error abbreviation traducao multipleTranslations\n                         | middle2_word_error no_hifen traducao multipleTranslations\n    \n    multipleTranslations : middle1_word traducao suffix_error_word traducao multipleTranslations\n                         | no_hifen traducao abbreviation traducao multipleTranslations\n                         | middle2_word traducao abbreviation traducao multipleTranslations\n                         | middle1_word traducao abbreviation traducao multipleTranslations\n    \n    multipleTranslations : no_hifen_paragraph no_hifen traducao multipleTranslations\n                         | no_hifen_paragraph abbreviation traducao multipleTranslations\n    \n    multipleTranslations : prefix_word traducao multipleTranslations\n                         | prefix_word_error traducao multipleTranslations\n                         | prefix_word_error_2 traducao multipleTranslations\n                         | prefix_word_error_2 baseword_error multipleTranslations\n                         | middle1_word traducao multipleTranslations\n                         | middle1_word_error_2 traducao multipleTranslations\n                         | middle_word_5 traducao multipleTranslations\n                         | middle2_word traducao multipleTranslations\n                         | suffix_word traducao multipleTranslations\n                         | suffix_error traducao multipleTranslations\n                         | double_word traducao multipleTranslations\n                         | prefix_error_word traducao multipleTranslations\n                         | middle_error_word traducao multipleTranslations\n                         | suffix_error_word traducao multipleTranslations  \n                         | no_hifen traducao multipleTranslations   \n                         | abbreviation traducao multipleTranslations\n    \n    multipleTranslations : middle1_word_error multipleTranslations\n                         | middle2_word_error multipleTranslations\n    multipleTranslations : \n    traducao : portugueseTranslationError\n             | portugueseTranslation\n    '
    
_lr_action_items = {'$end':([0,1,2,3,4,5,8,11,12,13,14,15,16,17,34,37,40,41,42,43,45,47,48,49,50,51,54,55,56,57,58,59,60,61,62,63,64,65,67,68,69,70,71,72,73,74,75,76,78,80,82,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,],[-2,0,-2,-14,-1,-3,-41,-14,-42,-43,-41,-41,-14,-41,-41,-4,-14,-14,-14,-10,-40,-41,-41,-41,-41,-41,-41,-41,-41,-41,-41,-41,-41,-41,-41,-41,-41,-39,-14,-14,-14,-14,-7,-8,-9,-41,-41,-38,-37,-27,-36,-30,-41,-41,-23,-24,-25,-26,-28,-29,-31,-32,-33,-34,-35,-14,-13,-12,-5,-6,-15,-16,-41,-41,-41,-41,-21,-22,-11,-18,-17,-20,-19,]),'initial_letter':([0,2,3,5,8,11,12,13,14,15,16,17,34,37,40,41,42,43,45,47,48,49,50,51,54,55,56,57,58,59,60,61,62,63,64,65,67,68,69,70,71,72,73,74,75,76,78,80,82,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,],[3,3,-14,-3,-41,-14,-42,-43,-41,-41,-14,-41,-41,-4,-14,-14,-14,-10,-40,-41,-41,-41,-41,-41,-41,-41,-41,-41,-41,-41,-41,-41,-41,-41,-41,-39,-14,-14,-14,-14,-7,-8,-9,-41,-41,-38,-37,-27,-36,-30,-41,-41,-23,-24,-25,-26,-28,-29,-31,-32,-33,-34,-35,-14,-13,-12,-5,-6,-15,-16,-41,-41,-41,-41,-21,-22,-11,-18,-17,-20,-19,]),'normalword':([3,8,11,12,13,14,15,16,17,34,40,41,42,45,47,48,49,50,51,54,55,56,57,58,59,60,61,62,63,64,65,67,68,69,70,74,75,76,78,80,82,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,103,104,105,106,107,108,109,110,112,113,114,115,],[6,-41,6,-42,-43,-41,-41,6,-41,-41,6,6,6,-40,-41,-41,-41,-41,-41,-41,-41,-41,-41,-41,-41,-41,-41,-41,-41,-41,-39,6,6,6,6,-41,-41,-38,-37,-27,-36,-30,-41,-41,-23,-24,-25,-26,-28,-29,-31,-32,-33,-34,-35,6,-15,-16,-41,-41,-41,-41,-21,-22,-18,-17,-20,-19,]),'baseword':([3,8,11,12,13,14,15,16,17,34,40,41,42,45,47,48,49,50,51,54,55,56,57,58,59,60,61,62,63,64,65,67,68,69,70,74,75,76,78,80,82,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,103,104,105,106,107,108,109,110,112,113,114,115,],[7,-41,7,-42,-43,-41,-41,7,-41,-41,7,7,7,-40,-41,-41,-41,-41,-41,-41,-41,-41,-41,-41,-41,-41,-41,-41,-41,-41,-39,7,7,7,7,-41,-41,-38,-37,-27,-36,-30,-41,-41,-23,-24,-25,-26,-28,-29,-31,-32,-33,-34,-35,7,-15,-16,-41,-41,-41,-41,-21,-22,-18,-17,-20,-19,]),'baseword_error':([3,8,11,12,13,14,15,16,17,26,34,35,40,41,42,45,47,48,49,50,51,54,55,56,57,58,59,60,61,62,63,64,65,67,68,69,70,74,75,76,78,80,82,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,103,104,105,106,107,108,109,110,112,113,114,115,],[8,-41,8,-42,-43,-41,-41,8,-41,57,-41,67,8,8,8,-40,-41,-41,-41,-41,-41,-41,-41,-41,-41,-41,-41,-41,-41,-41,-41,-41,-39,8,8,8,8,-41,-41,-38,-37,-27,-36,-30,-41,-41,-23,-24,-25,-26,-28,-29,-31,-32,-33,-34,-35,8,-15,-16,-41,-41,-41,-41,-21,-22,-18,-17,-20,-19,]),'a_parenteses':([3,8,11,12,13,14,15,16,17,34,40,41,42,45,47,48,49,50,51,54,55,56,57,58,59,60,61,62,63,64,65,67,68,69,70,74,75,76,78,80,82,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,103,104,105,106,107,108,109,110,112,113,114,115,],[9,-41,9,-42,-43,-41,-41,9,-41,-41,9,9,9,-40,-41,-41,-41,-41,-41,-41,-41,-41,-41,-41,-41,-41,-41,-41,-41,-41,-39,9,9,9,9,-41,-41,-38,-37,-27,-36,-30,-41,-41,-23,-24,-25,-26,-28,-29,-31,-32,-33,-34,-35,9,-15,-16,-41,-41,-41,-41,-21,-22,-18,-17,-20,-19,]),'a_parenteses_paragraph':([3,8,11,12,13,14,15,16,17,34,40,41,42,45,47,48,49,50,51,54,55,56,57,58,59,60,61,62,63,64,65,67,68,69,70,74,75,76,78,80,82,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,103,104,105,106,107,108,109,110,112,113,114,115,],[10,-41,10,-42,-43,-41,-41,10,-41,-41,10,10,10,-40,-41,-41,-41,-41,-41,-41,-41,-41,-41,-41,-41,-41,-41,-41,-41,-41,-39,10,10,10,10,-41,-41,-38,-37,-27,-36,-30,-41,-41,-23,-24,-25,-26,-28,-29,-31,-32,-33,-34,-35,10,-15,-16,-41,-41,-41,-41,-21,-22,-18,-17,-20,-19,]),'portugueseTranslationError':([6,7,8,9,18,19,20,21,22,24,25,26,27,28,29,30,31,32,33,36,38,39,44,46,52,53,66,77,79,81,83,],[12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,]),'portugueseTranslation':([6,7,8,9,18,19,20,21,22,24,25,26,27,28,29,30,31,32,33,36,38,39,44,46,52,53,66,77,79,81,83,],[13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,]),'middle2_word_error':([8,11,12,13,14,15,17,34,47,48,49,50,51,54,55,56,57,58,59,60,61,62,63,64,69,70,74,75,85,86,105,106,107,108,],[17,17,-42,-43,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,]),'middle1_word':([8,11,12,13,14,15,17,34,47,48,49,50,51,54,55,56,57,58,59,60,61,62,63,64,69,70,74,75,85,86,105,106,107,108,],[20,20,-42,-43,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,]),'no_hifen':([8,11,12,13,14,15,17,23,34,47,48,49,50,51,54,55,56,57,58,59,60,61,62,63,64,69,70,74,75,85,86,105,106,107,108,],[19,38,-42,-43,19,19,46,52,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,]),'middle2_word':([8,11,12,13,14,15,17,34,47,48,49,50,51,54,55,56,57,58,59,60,61,62,63,64,69,70,74,75,85,86,105,106,107,108,],[22,22,-42,-43,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,]),'no_hifen_paragraph':([8,11,12,13,14,15,17,34,47,48,49,50,51,54,55,56,57,58,59,60,61,62,63,64,69,70,74,75,85,86,105,106,107,108,],[23,23,-42,-43,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,]),'prefix_word':([8,11,12,13,14,15,17,34,47,48,49,50,51,54,55,56,57,58,59,60,61,62,63,64,69,70,74,75,85,86,105,106,107,108,],[24,24,-42,-43,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,]),'prefix_word_error':([8,11,12,13,14,15,17,34,47,48,49,50,51,54,55,56,57,58,59,60,61,62,63,64,69,70,74,75,85,86,105,106,107,108,],[25,25,-42,-43,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,]),'prefix_word_error_2':([8,11,12,13,14,15,17,34,47,48,49,50,51,54,55,56,57,58,59,60,61,62,63,64,69,70,74,75,85,86,105,106,107,108,],[26,26,-42,-43,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,]),'middle1_word_error_2':([8,11,12,13,14,15,17,34,47,48,49,50,51,54,55,56,57,58,59,60,61,62,63,64,69,70,74,75,85,86,105,106,107,108,],[27,27,-42,-43,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,]),'middle_word_5':([8,11,12,13,14,15,17,34,47,48,49,50,51,54,55,56,57,58,59,60,61,62,63,64,69,70,74,75,85,86,105,106,107,108,],[28,28,-42,-43,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,]),'suffix_word':([8,11,12,13,14,15,17,34,47,48,49,50,51,54,55,56,57,58,59,60,61,62,63,64,69,70,74,75,85,86,105,106,107,108,],[29,29,-42,-43,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,]),'suffix_error':([8,11,12,13,14,15,17,34,47,48,49,50,51,54,55,56,57,58,59,60,61,62,63,64,69,70,74,75,85,86,105,106,107,108,],[30,30,-42,-43,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,]),'double_word':([8,11,12,13,14,15,17,34,47,48,49,50,51,54,55,56,57,58,59,60,61,62,63,64,69,70,74,75,85,86,105,106,107,108,],[31,31,-42,-43,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,]),'prefix_error_word':([8,11,12,13,14,15,17,34,47,48,49,50,51,54,55,56,57,58,59,60,61,62,63,64,69,70,74,75,85,86,105,106,107,108,],[32,32,-42,-43,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,]),'middle_error_word':([8,11,12,13,14,15,17,34,47,48,49,50,51,54,55,56,57,58,59,60,61,62,63,64,69,70,74,75,85,86,105,106,107,108,],[33,33,-42,-43,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,]),'suffix_error_word':([8,11,12,13,14,15,17,34,47,48,49,50,51,54,55,56,57,58,59,60,61,62,63,64,69,70,74,75,85,86,105,106,107,108,],[21,21,-42,-43,21,21,21,21,21,21,79,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,]),'abbreviation':([8,11,12,13,14,15,17,23,34,47,48,49,50,51,54,55,56,57,58,59,60,61,62,63,64,69,70,74,75,85,86,105,106,107,108,],[18,39,-42,-43,18,18,44,53,18,18,77,81,18,83,18,18,18,18,18,18,18,18,18,18,18,77,18,18,77,18,18,18,18,18,18,]),'middle1_word_error':([8,11,12,13,14,15,17,34,47,48,49,50,51,54,55,56,57,58,59,60,61,62,63,64,69,70,74,75,85,86,105,106,107,108,],[34,34,-42,-43,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,]),'f_parenteses':([10,12,13,35,],[36,-42,-43,66,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'Dict':([0,2,],[1,4,]),'Alphsection':([0,2,],[2,2,]),'translations':([3,11,16,40,41,42,67,68,69,70,98,],[5,37,43,71,72,73,99,100,101,102,111,]),'traducao':([6,7,8,9,18,19,20,21,22,24,25,26,27,28,29,30,31,32,33,36,38,39,44,46,52,53,66,77,79,81,83,],[11,14,15,35,47,48,49,50,51,54,55,56,58,59,60,61,62,63,64,68,69,70,74,75,85,86,98,105,106,107,108,]),'multipleTranslations':([8,11,14,15,17,34,47,48,49,50,51,54,55,56,57,58,59,60,61,62,63,64,69,70,74,75,85,86,105,106,107,108,],[16,40,41,42,45,65,76,78,80,82,84,87,88,89,90,91,92,93,94,95,96,97,78,76,103,104,109,110,112,113,114,115,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> Dict","S'",1,None,None,None),
  ('Dict -> Alphsection Dict','Dict',2,'p_dict1','analisesintatica.py',29),
  ('Dict -> <empty>','Dict',0,'p_dict2','analisesintatica.py',35),
  ('Alphsection -> initial_letter translations','Alphsection',2,'p_Alphsection','analisesintatica.py',40),
  ('translations -> normalword traducao translations','translations',3,'p_translations1','analisesintatica.py',44),
  ('translations -> normalword traducao no_hifen traducao translations','translations',5,'p_translations2','analisesintatica.py',56),
  ('translations -> normalword traducao abbreviation traducao translations','translations',5,'p_translations2','analisesintatica.py',57),
  ('translations -> normalword traducao multipleTranslations translations','translations',4,'p_translations3','analisesintatica.py',82),
  ('translations -> baseword traducao multipleTranslations translations','translations',4,'p_translations4','analisesintatica.py',90),
  ('translations -> baseword_error traducao multipleTranslations translations','translations',4,'p_translations4','analisesintatica.py',91),
  ('translations -> baseword_error multipleTranslations translations','translations',3,'p_translations4','analisesintatica.py',92),
  ('translations -> a_parenteses traducao f_parenteses traducao translations','translations',5,'p_translations5','analisesintatica.py',112),
  ('translations -> a_parenteses_paragraph f_parenteses traducao translations','translations',4,'p_translations5','analisesintatica.py',113),
  ('translations -> a_parenteses traducao baseword_error translations','translations',4,'p_translations6','analisesintatica.py',145),
  ('translations -> <empty>','translations',0,'p_translations7','analisesintatica.py',160),
  ('multipleTranslations -> middle2_word_error abbreviation traducao multipleTranslations','multipleTranslations',4,'p_multipleTranslations3','analisesintatica.py',172),
  ('multipleTranslations -> middle2_word_error no_hifen traducao multipleTranslations','multipleTranslations',4,'p_multipleTranslations3','analisesintatica.py',173),
  ('multipleTranslations -> middle1_word traducao suffix_error_word traducao multipleTranslations','multipleTranslations',5,'p_multipleTranslations4','analisesintatica.py',201),
  ('multipleTranslations -> no_hifen traducao abbreviation traducao multipleTranslations','multipleTranslations',5,'p_multipleTranslations4','analisesintatica.py',202),
  ('multipleTranslations -> middle2_word traducao abbreviation traducao multipleTranslations','multipleTranslations',5,'p_multipleTranslations4','analisesintatica.py',203),
  ('multipleTranslations -> middle1_word traducao abbreviation traducao multipleTranslations','multipleTranslations',5,'p_multipleTranslations4','analisesintatica.py',204),
  ('multipleTranslations -> no_hifen_paragraph no_hifen traducao multipleTranslations','multipleTranslations',4,'p_multipleTranslations5','analisesintatica.py',220),
  ('multipleTranslations -> no_hifen_paragraph abbreviation traducao multipleTranslations','multipleTranslations',4,'p_multipleTranslations5','analisesintatica.py',221),
  ('multipleTranslations -> prefix_word traducao multipleTranslations','multipleTranslations',3,'p_multipleTranslations6','analisesintatica.py',239),
  ('multipleTranslations -> prefix_word_error traducao multipleTranslations','multipleTranslations',3,'p_multipleTranslations6','analisesintatica.py',240),
  ('multipleTranslations -> prefix_word_error_2 traducao multipleTranslations','multipleTranslations',3,'p_multipleTranslations6','analisesintatica.py',241),
  ('multipleTranslations -> prefix_word_error_2 baseword_error multipleTranslations','multipleTranslations',3,'p_multipleTranslations6','analisesintatica.py',242),
  ('multipleTranslations -> middle1_word traducao multipleTranslations','multipleTranslations',3,'p_multipleTranslations6','analisesintatica.py',243),
  ('multipleTranslations -> middle1_word_error_2 traducao multipleTranslations','multipleTranslations',3,'p_multipleTranslations6','analisesintatica.py',244),
  ('multipleTranslations -> middle_word_5 traducao multipleTranslations','multipleTranslations',3,'p_multipleTranslations6','analisesintatica.py',245),
  ('multipleTranslations -> middle2_word traducao multipleTranslations','multipleTranslations',3,'p_multipleTranslations6','analisesintatica.py',246),
  ('multipleTranslations -> suffix_word traducao multipleTranslations','multipleTranslations',3,'p_multipleTranslations6','analisesintatica.py',247),
  ('multipleTranslations -> suffix_error traducao multipleTranslations','multipleTranslations',3,'p_multipleTranslations6','analisesintatica.py',248),
  ('multipleTranslations -> double_word traducao multipleTranslations','multipleTranslations',3,'p_multipleTranslations6','analisesintatica.py',249),
  ('multipleTranslations -> prefix_error_word traducao multipleTranslations','multipleTranslations',3,'p_multipleTranslations6','analisesintatica.py',250),
  ('multipleTranslations -> middle_error_word traducao multipleTranslations','multipleTranslations',3,'p_multipleTranslations6','analisesintatica.py',251),
  ('multipleTranslations -> suffix_error_word traducao multipleTranslations','multipleTranslations',3,'p_multipleTranslations6','analisesintatica.py',252),
  ('multipleTranslations -> no_hifen traducao multipleTranslations','multipleTranslations',3,'p_multipleTranslations6','analisesintatica.py',253),
  ('multipleTranslations -> abbreviation traducao multipleTranslations','multipleTranslations',3,'p_multipleTranslations6','analisesintatica.py',254),
  ('multipleTranslations -> middle1_word_error multipleTranslations','multipleTranslations',2,'p_multipleTranslations9','analisesintatica.py',262),
  ('multipleTranslations -> middle2_word_error multipleTranslations','multipleTranslations',2,'p_multipleTranslations9','analisesintatica.py',263),
  ('multipleTranslations -> <empty>','multipleTranslations',0,'p_multipleTranslations8','analisesintatica.py',269),
  ('traducao -> portugueseTranslationError','traducao',1,'p_traducao','analisesintatica.py',274),
  ('traducao -> portugueseTranslation','traducao',1,'p_traducao','analisesintatica.py',275),
]
