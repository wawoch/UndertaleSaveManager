import cmd
from colorama import init, Fore, Style
import os
import time
import configparser
import pathlib


init(autoreset=True)

romids = '''
0	room_start
1	room_introstory
2	room_introimage
3	room_intromenu
4	room_area1
5	room_area1_2
6	room_ruins1
7	room_ruins2
8	room_ruins3
9	room_ruins4
10	room_ruins5
11	room_ruins6
12	room_ruins7
13	room_ruins7A
14	room_ruins8
15	room_ruins9
16	room_ruins10
17	room_ruins11
18	room_ruins12A
19	room_ruins12
20	room_ruins12B
21	room_ruins13
22	room_ruins14
23	room_ruins15A
24	room_ruins15B
25	room_ruins15C
26	room_ruins15D
27	room_ruins15E
28	room_ruins16
29	room_ruins17
30	room_ruins18OLD
31	room_ruins19
32	room_torhouse1
33	room_torhouse2
34	room_torhouse3
35	room_torielroom
36	room_asrielroom
37	room_kitchen
38	room_basement1
39	room_basement2
40	room_basement3
41	room_basement4
42	room_basement5
43	room_ruinsexit
44	room_tundra1
45	room_tundra2
46	room_tundra3
47	room_tundra3A
48	room_tundra4
49	room_tundra5
50	room_tundra6
51	room_tundra6A
52	room_tundra7
53	room_tundra8
54	room_tundra8A
55	room_tundra9
56	room_tundra_spaghetti
57	room_tundra_snowpuzz
58	room_tundra_xoxosmall
59	room_tundra_xoxopuzz
60	room_tundra_randoblock
61	room_tundra_lesserdog
62	room_tundra_icehole
63	room_tundra_iceentrance
64	room_tundra_iceexit_new
65	room_tundra_iceexit
66	room_tundra_poffzone
67	room_tundra_dangerbridge
68	room_tundra_town
69	room_tundra_town2
70	room_tundra_dock
71	room_tundra_inn
72	room_tundra_inn_2f
73	room_tundra_grillby
74	room_tundra_library
75	room_tundra_garage
76	room_tundra_sanshouse
77	room_tundra_paproom
78	room_tundra_sansroom
79	room_tundra_sansroom_dark
80	room_tundra_sansbasement
81	room_fogroom
82	room_water1
83	room_water2
84	room_water3
85	room_water3A
86	room_water4
87	room_water_bridgepuzz1
88	room_water5
89	room_water5A
90	room_water6
91	room_water7
92	room_water8
93	room_water9
94	room_water_savepoint1
95	room_water11
96	room_water_nicecream
97	room_water12
98	room_water_shoe
99	room_water_bird
100	room_water_onionsan
101	room_water14
102	room_water_piano
103	room_water_dogroom
104	room_water_statue
105	room_water_prewaterfall
106	room_water_waterfall
107	room_water_waterfall2
108	room_water_waterfall3
109	room_water_waterfall4
110	room_water_preundyne
111	room_water_undynebridge
112	room_water_undynebridgeend
113	room_water_trashzone1
114	room_water_trashsavepoint
115	room_water_trashzone2
116	room_water_friendlyhub
117	room_water_undyneyard
118	room_water_undynehouse
119	room_water_blookyard
120	room_water_blookhouse
121	room_water_hapstablook
122	room_water_farm
123	room_water_prebird
124	room_water_shop
125	room_water_dock
126	room_water15
127	room_water16
128	room_water_temvillage
129	room_water17
130	room_water18
131	room_water19
132	room_water20
133	room_water21
134	room_water_undynefinal
135	room_water_undynefinal2
136	room_water_undynefinal3
137	room_fire1
138	room_fire2
139	room_fire_prelab
140	room_fire_dock
141	room_fire_lab1
142	room_fire_lab2
143	room_fire3
144	room_fire5
145	room_fire6
146	room_fire6A
147	room_fire_lasers1
148	room_fire7
149	room_fire8
150	room_fire_shootguy_2
151	room_fire9
152	room_fire_shootguy_1
153	room_fire_turn
154	room_fire_cookingshow
155	room_fire_savepoint1
156	room_fire_elevator_r1
157	room_fire_elevator_r2
158	room_fire_hotdog
159	room_fire_walkandbranch
160	room_fire_sorry
161	room_fire_apron
162	room_fire10
163	room_fire_rpuzzle
164	room_fire_mewmew2
165	room_fire_boysnightout
166	room_fire_newsreport
167	room_fire_coreview2
168	room_fire_elevator_l2
169	room_fire_elevator_l3
170	room_fire_spidershop
171	room_fire_walkandbranch2
172	room_fire_conveyorlaser
173	room_fire_shootguy_3
174	room_fire_preshootguy4
175	room_fire_shootguy_4
176	room_fire_savepoint2
177	room_fire_spider
178	room_fire_pacing
179	room_fire_operatest
180	room_fire_multitile
181	room_fire_hotelfront_1
182	room_fire_hotelfront_2
183	room_fire_hotellobby
184	room_fire_restaurant
185	room_fire_hoteldoors
186	room_fire_hotelbed
187	room_fire_elevator_r3
188	room_fire_precore
189	room_fire_core1
190	room_fire_core2
191	room_fire_core3
192	room_fire_core4
193	room_fire_core5
194	room_fire_core_freebattle
195	room_fire_core_laserfun
196	room_fire_core_branch
197	room_fire_core_bottomleft
198	room_fire_core_left
199	room_fire_core_topleft
200	room_fire_core_top
201	room_fire_core_topright
202	room_fire_core_right
203	room_fire_core_bottomright
204	room_fire_core_center
205	room_fire_shootguy_5
206	room_fire_core_treasureleft
207	room_fire_core_treasureright
208	room_fire_core_warrior
209	room_fire_core_bridge
210	room_fire_core_premett
211	room_fire_core_metttest
212	room_fire_core_final
213	room_fire_elevator
214	room_fire_elevator_l1
215	room_fire_finalelevator
216	room_castle_elevatorout
217	room_castle_precastle
218	room_castle_hook
219	room_castle_front
220	room_asghouse1
221	room_asghouse2
222	room_asghouse3
223	room_asgoreroom
224	room_asrielroom_final
225	room_kitchen_final
226	room_basement1_final
227	room_basement2_final
228	room_basement3_final
229	room_basement4_final
230	room_lastruins_corridor
231	room_sanscorridor
232	room_castle_finalshoehorn
233	room_castle_coffins1
234	room_castle_coffins2
235	room_castle_throneroom
236	room_castle_prebarrier
237	room_castle_barrier
238	room_castle_exit
239	room_undertale_end
240	room_castle_trueexit
241	room_outsideworld
242	room_fire_labelevator
243	room_truelab_elevatorinside
244	room_truelab_elevator
245	room_truelab_hall1
246	room_truelab_hub
247	room_truelab_hall2
248	room_truelab_operatingroom
249	room_truelab_redlever
250	room_truelab_prebed
251	room_truelab_bedroom
252	room_truelab_mirror
253	room_truelab_bluelever
254	room_truelab_hall3
255	room_truelab_shower
256	room_truelab_determination
257	room_truelab_tv
258	room_truelab_cooler
259	room_truelab_greenlever
260	room_truelab_fan
261	room_truelab_castle_elevator
262	room_truelab_prepower
263	room_truelab_power
264	room_gaster
265	room_icecave1
266	room_ice_dog
267	room2
268	room_water_fakehallway
269	room_mysteryman
270	room_soundtest
271	TESTROOM
272	room_water_redacted
273	room_water13
274	room_overworld
275	room_overworld3
276	bullettest
277	room_water16A
278	room_end_castroll
279	room_end_highway
280	room_end_beach
281	room_end_metta
282	room_end_school
283	room_end_mtebott
284	room_creditsdodger
285	room_end_myroom
286	room_end_theend
287	room_spritecheck
288	room_joyconfig
289	room_controltest
290	room_f_start
291	room_f_intro
292	room_f_menu
293	room_f_room
294	room_floweyx
295	room_f_phrase
296	room_fire4
297	room_fire10_old
298	room_fire10A_old
299	room_tundra_placeholder
300	room_ruins12B_old
301	room_tundra_rollsnow
302	room_water7_older
303	room_meetundyne_old
304	room_water_mushroom
305	room_monsteralign_test
306	room_battle
307	room_floweybattle
308	room_fastbattle
309	room_storybattle
310	room_gameover
311	room_shop1
312	room_shop2
313	room_shop3
314	room_shop4
315	room_shop5
316	room_riverman_transition
317	room_papdate
318	room_adate
319	room_flowey_endchoice
320	room_flowey_regret
321	room_empty
322	room_emptywhite
323	room_emptyblack
324	room_nothingness
325	room_undertale
326	room_of_dog
327	room_quizholder
328	room_friendtest
329	room_bringitinguys
330	room_asrielappears
331	room_goodbyeasriel
332	room_asrielmemory
333	room_asrieltest
334	room_afinaltest
'''


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

class Console(cmd.Cmd):
    wlauncher = fr'''{Fore.LIGHTYELLOW_EX}{Style.BRIGHT}


                       __  __     ______     __    __    
                      /\ \/\ \   /\  ___\   /\ "-./  \   
                      \ \ \_\ \  \ \___  \  \ \ \-./\ \  
                       \ \_____\  \/\_____\  \ \_\ \ \_\ 
                        \/_____/   \/_____/   \/_/  \/_/ 

                            Undertale Save Manager
                                by wawa | v2.3

    {Fore.LIGHTBLACK_EX}1 - Изменить FUN  |  2 - Изменить кол-во золота  |  3 - Изменить LV  |  4 - Изменить HP  |  5 - Изменить Имя
    {Fore.LIGHTBLACK_EX}                      6 - Изменить кол-во опыта  |  7 - Далее..
    {Style.RESET_ALL} '''
    prompt = f"{Fore.YELLOW}usm-wawa@root{Fore.WHITE}:{Fore.YELLOW}~{Fore.WHITE}$ {Style.RESET_ALL}"

    def do_printpath(self, arg: str):
        print(pathlib.Path().absolute())

# Change FUN
    def do_1(self, arg: str):
        local = os.getenv('LOCALAPPDATA')
        undertale = 'UNDERTALE'
        
        funedit = input(f"{Fore.LIGHTYELLOW_EX}Введите новое значение FUN: {Style.RESET_ALL}")
        if not funedit.isdigit():
            print(f"{Fore.RED}Введите значение цифрами!{Style.RESET_ALL}")
            return
        else:
            if funedit == "":
                print(f"{Fore.RED}Введите значение!{Style.RESET_ALL}")
                return
            else:
                from os.path import expanduser
                home = expanduser("~")
                config = configparser.ConfigParser()
                config.optionxform = str
                config_file = os.path.join(home, 'AppData', 'Local', undertale, 'undertale.ini')
                config.read(config_file)
                if not config.has_section('General'):
                    config.add_section('General')
                config.set('General', 'fun', funedit + '.000000')

                with open(config_file, 'w') as configfile:
                    config.write(configfile)
            # change fun in file0
                with open(os.path.join(local, undertale, 'file0'), 'r+', encoding='utf-8') as f:
                    lines = f.readlines()
                    content = f.read()
                    lines[35] = f'{funedit}\n'
                    f.seek(0)
                    f.writelines(lines)
                    f.truncate()
                with open(os.path.join(local, undertale, 'file9'), 'r+', encoding='utf-8') as f:
                    lines = f.readlines()
                    content = f.read()
                    lines[35] = f'{funedit}\n'
                    f.seek(0)
                    f.writelines(lines)
                    f.truncate()
                print(f"{Fore.GREEN}FUN изменен на {Fore.LIGHTYELLOW_EX}{funedit}{Style.RESET_ALL}")
    def do_2(self, arg: str):
        local = os.getenv('LOCALAPPDATA')
        undertale = 'UNDERTALE'
        goldedit = input(f"{Fore.LIGHTYELLOW_EX}Введите новое кол-во золота: {Style.RESET_ALL}")
        if not goldedit.isdigit():
            print(f"{Fore.RED}Введите значение цифрами!{Style.RESET_ALL}")
            return
        else:
            if goldedit == "":
                print(f"{Fore.RED}Введите значение!{Style.RESET_ALL}")
                return
            else:
                with open(os.path.join(local, undertale, 'file0'), 'r+', encoding='utf-8') as f:
                    lines = f.readlines()
                    content = f.read()
                    lines[10] = f'{goldedit}\n'
                    f.seek(0)
                    f.writelines(lines)
                    f.truncate()
                with open(os.path.join(local, undertale, 'file9'), 'r+', encoding='utf-8') as f:
                    lines = f.readlines()
                    content = f.read()
                    lines[10] = f'{goldedit}\n'
                    f.seek(0)
                    f.writelines(lines)
                    f.truncate()
                print(f"{Fore.GREEN}Кол-во золота изменено на {Fore.LIGHTYELLOW_EX}{goldedit}{Style.RESET_ALL}")
    def do_4(self, arg: str):
        local = os.getenv('LOCALAPPDATA')
        undertale = 'UNDERTALE'
        hpedit = input(f"{Fore.LIGHTYELLOW_EX}Введите новое кол-во HP (не больше 111): {Style.RESET_ALL}")
        if not hpedit.isdigit():
            print(f"{Fore.RED}Введите значение цифрами!{Style.RESET_ALL}")
        else:
            if hpedit == "":
                print(f"{Fore.RED}Введите значение!{Style.RESET_ALL}")
                return
            else:
                with open(os.path.join(local, undertale, 'file0'), 'r+', encoding='utf-8') as f:
                    lines = f.readlines()
                    content = f.read()
                    lines[2] = f'{hpedit}\n'
                    f.seek(0)
                    f.writelines(lines)
                    f.truncate()
                with open(os.path.join(local, undertale, 'file9'), 'r+', encoding='utf-8') as f:
                    lines = f.readlines()
                    content = f.read()
                    lines[2] = f'{hpedit}\n'
                    f.seek(0)
                    f.writelines(lines)
                    f.truncate()
                print(f"{Fore.GREEN}Кол-во HP изменено на {Fore.LIGHTYELLOW_EX}{hpedit}{Style.RESET_ALL}")
    def do_3(self, arg: str):
        local = os.getenv('LOCALAPPDATA')
        undertale = 'UNDERTALE'
        
        lvedit = input(f"{Fore.LIGHTYELLOW_EX}Введите новый LV: {Style.RESET_ALL}")
        if not lvedit.isdigit():
            print(f"{Fore.RED}Введите значение цифрами!{Style.RESET_ALL}")
            return
        else:
            if lvedit == "":
                print(f"{Fore.RED}Введите значение!{Style.RESET_ALL}")
                return
            else:
                from os.path import expanduser
                home = expanduser("~")
                config = configparser.ConfigParser()
                config.optionxform = str
                config_file = os.path.join(home, 'AppData', 'Local', undertale, 'undertale.ini')
                config.read(config_file)
                config.set('General', 'Love', f"\"{lvedit}.000000\"")

                with open(config_file, 'w') as configfile:
                    config.write(configfile)

                with open(os.path.join(local, undertale, 'file0'), 'r+', encoding='utf-8') as f:
                    lines = f.readlines()
                    content = f.read()
                    lines[1] = f'{lvedit}\n'
                    f.seek(0)
                    f.writelines(lines)
                    f.truncate()
                with open(os.path.join(local, undertale, 'file9'), 'r+', encoding='utf-8') as f:
                    lines = f.readlines()
                    content = f.read()
                    lines[1] = f'{lvedit}\n'
                    f.seek(0)
                    f.writelines(lines)
                    f.truncate()
                print(f"{Fore.GREEN}LV изменен на {Fore.LIGHTYELLOW_EX}{lvedit}{Style.RESET_ALL}")
    def do_5(self, arg: str):
        local = os.getenv('LOCALAPPDATA')
        undertale = 'UNDERTALE'

        nameedit = input(f"{Fore.LIGHTYELLOW_EX}Введите новое имя (англ): {Style.RESET_ALL}")
        if nameedit.isdigit():
            print(f"{Fore.RED}Введите значение без цифр!{Style.RESET_ALL}")
        else:
            if nameedit == "":
                print(f"{Fore.RED}Введите значение!{Style.RESET_ALL}")
                return
            else:
                from os.path import expanduser
                home = expanduser("~")
                config = configparser.ConfigParser()
                config.optionxform = str
                config_file = os.path.join(home, 'AppData', 'Local', undertale, 'undertale.ini')
                config.read(config_file)
                config.set('General', 'Name', f"\"{nameedit}\"")

                with open(config_file, 'w') as configfile:
                    config.write(configfile)
                with open(os.path.join(local, undertale, 'file0'), 'r+', encoding='utf-8') as f:
                    lines = f.readlines()
                    content = f.read()
                    lines[0] = f'{nameedit}\n'
                    f.seek(0)
                    f.writelines(lines)
                    f.truncate()
                with open(os.path.join(local, undertale, 'file9'), 'r+', encoding='utf-8') as f:
                    lines = f.readlines()
                    content = f.read()
                    lines[0] = f'{nameedit}\n'
                    f.seek(0)
                    f.writelines(lines)
                    f.truncate()
                print(f"{Fore.GREEN}Имя изменено на {Fore.LIGHTYELLOW_EX}{nameedit}{Style.RESET_ALL}")
    def do_6(self, arg: str):
        local = os.getenv('LOCALAPPDATA')
        undertale = 'UNDERTALE'

        expedit = input(f"{Fore.LIGHTYELLOW_EX}Введите новое кол-во опыта: {Style.RESET_ALL}")
        if not expedit.isdigit():
            print(f"{Fore.RED}Введите значение цифрами!{Style.RESET_ALL}")
            return
        else:
            if expedit == "":
                print(f"{Fore.RED}Введите значение!{Style.RESET_ALL}")
                return
            else:
                with open(os.path.join(local, undertale, 'file0'), 'r+', encoding='utf-8') as f:
                    lines = f.readlines()
                    content = f.read()
                    lines[9] = f'{expedit}\n'
                    f.seek(0)
                    f.writelines(lines)
                    f.truncate()
                with open(os.path.join(local, undertale, 'file9'), 'r+', encoding='utf-8') as f:
                    lines = f.readlines()
                    content = f.read()
                    lines[9] = f'{expedit}\n'
                    f.seek(0)
                    f.writelines(lines)
                    f.truncate()
                print(f"{Fore.GREEN}Кол-во опыта изменено на {Fore.LIGHTYELLOW_EX}{expedit}{Style.RESET_ALL}")
    def do_7(self, arg: str):
        clear_console()
        print(fr'''{Fore.LIGHTYELLOW_EX}{Style.BRIGHT}


                       __  __     ______     __    __    
                      /\ \/\ \   /\  ___\   /\ "-./  \   
                      \ \ \_\ \  \ \___  \  \ \ \-./\ \  
                       \ \_____\  \/\_____\  \ \_\ \ \_\ 
                        \/_____/   \/_____/   \/_/  \/_/ 
                                   
                            Undertale Save Manager
                                by wawa | v2.2

    {Fore.LIGHTBLACK_EX}8 - Изменить кол-во убийств  |  9 - Зонт  |  10 - Конец игры?  |  11 - Геноцид?  |  12 - Изменить ID текущей комнаты
    {Fore.LIGHTBLACK_EX}                                             {Fore.LIGHTRED_EX}14 - Редактор инвентаря
    {Style.RESET_ALL} ''')
    
    def do_8(self, arg: str):
        local = os.getenv('LOCALAPPDATA')
        undertale = 'UNDERTALE'
        killedit = input(f"{Fore.LIGHTYELLOW_EX}Введите новое кол-во убийств: {Style.RESET_ALL}")
        if not killedit.isdigit():
            print(f"{Fore.RED}Введите значение цифрами!{Style.RESET_ALL}")
            return
        else:
            if killedit == "":
                print(f"{Fore.RED}Введите значение!{Style.RESET_ALL}")
                return
            else:
                from os.path import expanduser
                home = expanduser("~")
                config = configparser.ConfigParser()
                config.optionxform = str
                config_file = os.path.join(home, 'AppData', 'Local', undertale, 'undertale.ini')
                config.read(config_file)
                config.set('General', 'Kills', f"\"{killedit}.000000\"")

                with open(config_file, 'w') as configfile:
                    config.write(configfile)

                with open(os.path.join(local, undertale, 'file0'), 'r+', encoding='utf-8') as f:
                    lines = f.readlines()
                    content = f.read()
                    lines[11] = f'{killedit}\n'
                    f.seek(0)
                    f.writelines(lines)
                    f.truncate()
                with open(os.path.join(local, undertale, 'file9'), 'r+', encoding='utf-8') as f:
                    lines = f.readlines()
                    content = f.read()
                    lines[11] = f'{killedit}\n'
                    f.seek(0)
                    f.writelines(lines)
                    f.truncate()
                print(f"{Fore.GREEN}Кол-во убийств изменено на {Fore.LIGHTYELLOW_EX}{killedit}{Style.RESET_ALL}")
    def do_9(self, arg: str):
        local = os.getenv('LOCALAPPDATA')
        undertale = 'UNDERTALE'
        zoneedit = input(f"{Fore.LIGHTYELLOW_EX}У игрока будет зонт? Y/N - {Style.RESET_ALL}")
        if zoneedit == "y":
            with open(os.path.join(local, undertale, 'file0'), 'r+', encoding='utf-8') as f:
                lines = f.readlines()   
                content = f.read()
                lines[115] = f'1\n'
                f.seek(0)
                f.writelines(lines)
                f.truncate()    
            with open(os.path.join(local, undertale, 'file9'), 'r+', encoding='utf-8') as f:
                lines = f.readlines()
                content = f.read()
                lines[115] = f'1\n'
                f.seek(0)
                f.writelines(lines)
                f.truncate()
            print(f"{Fore.GREEN}Зонт выдан! {Fore.LIGHTYELLOW_EX}{zoneedit}{Style.RESET_ALL}")    
        elif zoneedit == "n":
            with open(os.path.join(local, undertale, 'file0'), 'r+', encoding='utf-8') as f:
                lines = f.readlines()   
                content = f.read()
                lines[115] = f'0\n'
                f.seek(0)
                f.writelines(lines)
                f.truncate()    
            with open(os.path.join(local, undertale, 'file9'), 'r+', encoding='utf-8') as f:
                lines = f.readlines()
                content = f.read()
                lines[115] = f'0\n'
                f.seek(0)
                f.writelines(lines)
                f.truncate()
            print(f"{Fore.GREEN}Зонт убран! {Fore.LIGHTYELLOW_EX}{zoneedit}{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}Введите Y или N!{Style.RESET_ALL}")
            return
    def do_10(self, arg: str):
        local = os.getenv('LOCALAPPDATA')
        undertale = 'UNDERTALE'
        endedit = input(f"{Fore.LIGHTYELLOW_EX}Разрушить барьер? Y/N - {Style.RESET_ALL}")
        if endedit == "y":
            with open(os.path.join(local, undertale, 'file0'), 'r+', encoding='utf-8') as f:
                lines = f.readlines()
                content = f.read()
                lines[37] = f'1\n'
                f.seek(0)
                f.writelines(lines)
                f.truncate()
            with open(os.path.join(local, undertale, 'file9'), 'r+', encoding='utf-8') as f:
                lines = f.readlines()
                content = f.read()
                lines[37] = f'1\n'
                f.seek(0)
                f.writelines(lines)
                f.truncate()
            print(f"{Fore.GREEN}Барьер был разрушен. {Fore.LIGHTYELLOW_EX}{endedit}{Style.RESET_ALL}")
        elif endedit == "n":
            with open(os.path.join(local, undertale, 'file0'), 'r+', encoding='utf-8') as f:
                lines = f.readlines()
                content = f.read()
                lines[37] = f'0\n'
                f.seek(0)
                f.writelines(lines)
                f.truncate()
            with open(os.path.join(local, undertale, 'file9'), 'r+', encoding='utf-8') as f:
                lines = f.readlines()
                content = f.read()
                lines[37] = f'0\n'
                f.seek(0)
                f.writelines(lines)
                f.truncate()
            print(f"{Fore.GREEN}Барьер восстановлен или не был разрушен! {Fore.LIGHTYELLOW_EX}{endedit}{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}Введите Y или N!{Style.RESET_ALL}")
            return
    def do_11(self, arg: str):
        local = os.getenv('LOCALAPPDATA')
        undertale = 'UNDERTALE'
        genedit = input(f"{Fore.LIGHTYELLOW_EX}Активировать геноцид? Y/N - {Style.RESET_ALL}")
        if genedit == "y":
            with open(os.path.join(local, undertale, 'file0'), 'r+', encoding='utf-8') as f:
                lines = f.readlines()
                content = f.read()
                lines[510] = f'1\n'
                f.seek(0)
                f.writelines(lines)
                f.truncate()
            with open(os.path.join(local, undertale, 'file9'), 'r+', encoding='utf-8') as f:
                lines = f.readlines()
                content = f.read()
                lines[510] = f'1\n'
                f.seek(0)
                f.writelines(lines)
                f.truncate()
            print(f"{Fore.GREEN}Геноцид активирован! {Fore.LIGHTYELLOW_EX}{genedit}{Style.RESET_ALL}")
        elif genedit == "n":
            with open(os.path.join(local, undertale, 'file0'), 'r+', encoding='utf-8') as f:
                lines = f.readlines()
                content = f.read()
                lines[510] = f'0\n'
                f.seek(0)
                f.writelines(lines)
                f.truncate()
            with open(os.path.join(local, undertale, 'file9'), 'r+', encoding='utf-8') as f:
                lines = f.readlines()
                content = f.read()
                lines[510] = f'0\n'
                f.seek(0)
                f.writelines(lines)
                f.truncate()
            print(f"{Fore.GREEN}Геноцид деактивирован! {Fore.LIGHTYELLOW_EX}{genedit}{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}Введите Y или N!{Style.RESET_ALL}")
            return
    def do_14(self, arg: str):
        print(f'''\n{Fore.LIGHTRED_EX}1-7 - Слоты инвентаря | 8 - Слот Оружия | 9 - Слот Брони\n{Style.RESET_ALL}''')
        slotid = 0
        slot = input(f"{Fore.LIGHTYELLOW_EX}Введите номер слота: {Style.RESET_ALL}")
        if slot == "1":
            slotid = "12"
        elif slot == "2":
            slotid = "14"
        elif slot == "3":
            slotid = "16"
        elif slot == "4":
            slotid = "18"
        elif slot == "5":
            slotid = "20"
        elif slot == "6":
            slotid = "22"
        elif slot == "7":
            slotid = "24"
        elif slot == "8":
            slotid = "28"
        elif slot == "9":
            slotid = "29"
        else:
            print(f"{Fore.RED}Введите значение от 1 до 9!{Style.RESET_ALL}")
            return
        local = os.getenv('LOCALAPPDATA')
        undertale = 'UNDERTALE'
        print(f'''
{Fore.WHITE}ID всех предметов.{Fore.LIGHTBLACK_EX}
    1 - Monster Candy (Монстр Конфета)
    2 - Croquet Roll (Крокет Ролл)
    3 - Stick (Палка)
    4 - Bandage (Пластырь)
    5 - Rock Candy (Каменная Конфета)
    6 - Pumpkin Rings (Тыквенные Кольца)
    7 - Spider Donut (Паучий Пончик)
    8 - Stoic Onion	(Твёрдый Лук)
    9 - Ghost Fruit	(Призрачный Фрукт)
    10 - Spider Cider (Паучий Сидр)
    11 - Butterscotch Pie (Ирисковый Пирог)
    12 - Faded Ribbon (Выцветшая Лента)
    13 - Toy Knife (Игрушечный Нож)
    14 - Tough Glove (Грубая Перчатка)
    15 - Manly Bandanna	(Мужская бандана)
    16 - Snowman Piece (Кусочек Снеговика)
    17 - Nice Cream	(Доброженое)
    18 - Puppydough Icecream (Мороженое с тестом щенка)
    19 - Bisicle (Дваскимо)
    20 - Unisicle (Односкимо)
    21 - Cinnamon Bun (Коричный кролик)	
    22 - Temmie Flakes	(Хлопья Темми)
    23 - Abandoned Quiche (Брошенный киш)
    24 - Old Tutu (Старая пачка)
    25 - Ballet Shoes (Балетки)
    26 - Punch Card	(Ударная карта)
    27 - Annoying Dog (Надоедливая собака)
    28 - Dog Salad (Собачий салат)
    29-34 - Dog Residue	(Собачьи остатки)
    35 - Astronaut Food	(Еда астронавтов)
    36 - Instant Noodles (Лапша Б.П)
    37 - Crab Apple	(Крабовое Яблоко)
    38 - Hot Dog...? (Хот-Дог...?)
    39 - Hot Cat	(Хот-кэт)
    40 - Glamburger (Гламбургер)
    41 - Sea Tea	(Морской чай)
    42 - Starfait (Звёздофе)
    43 - Legendary Hero	(Легендарный герой)
    44 - Cloudy Glasses	(Мутные очки)
    45 - Torn Notebook	(Порванная тетрадь)
    46 - Stained Apron	(Запачканный фартук)
    47 - Burnt Pan	(Подгоревшая сковорода)
    48 - Cowboy Hat	(Ковбойская шляпа)
    49 - Empty Gun	(Пустой пистолет)
    50 - Heart Locket (Медальон в форме сердца)
    51 - Worn Dagger (Изношенный кинжал)
    52 - Real Knife	(Настоящий нож)
    53 - The Locket (Медальон)
    54 - Bad Memory	(Плохое воспоминание)
    55 - Dream (Последняя мечта)
    56 - Undyne's Letter (Письмо Андайн)
    57 - Undyne Letter EX (Письмо Андайн EX)
    58 - Popato Chisps (Катрофельные Чиспы)
    59 - Junk Food (Вредная еда)
    60 - Mystery Key (Таинственный ключ)
    61 - Face Steak	(Стейк-Лицо)
    62 - Hush Puppy	(Тихий щенок)
    63 - Snail Pie	(Улиточный пирог)
    64 - temy armor	(броня теми)
{Style.RESET_ALL}''')
        itemedit = input(f"{Fore.LIGHTYELLOW_EX}Введите ID предмета: {Style.RESET_ALL}")
        if not itemedit.isdigit():
            print(f"{Fore.RED}Введите значение цифрами!{Style.RESET_ALL}")
            return
        else:
            if itemedit == "":
                print(f"{Fore.RED}Введите значение!{Style.RESET_ALL}")
                return
            elif int(itemedit) >= 65:
                print(f"{Fore.RED}Введите значение меньше 65!{Style.RESET_ALL}")
                return
            else:
                with open(os.path.join(local, undertale, 'file0'), 'r+', encoding='utf-8') as f:
                    lines = f.readlines()
                    content = f.read()
                    lines[int(slotid)] = f'{itemedit}\n'
                    f.seek(0)
                    f.writelines(lines)
                    f.truncate()
                with open(os.path.join(local, undertale, 'file9'), 'r+', encoding='utf-8') as f:
                    lines = f.readlines()
                    content = f.read()
                    lines[int(slotid)] = f'{itemedit}\n'
                    f.seek(0)
                    f.writelines(lines)
                    f.truncate()
                clear_console()
                time.sleep(0.1)
                print(fr'''{Fore.LIGHTYELLOW_EX}{Style.BRIGHT}


                       __  __     ______     __    __    
                      /\ \/\ \   /\  ___\   /\ "-./  \   
                      \ \ \_\ \  \ \___  \  \ \ \-./\ \  
                       \ \_____\  \/\_____\  \ \_\ \ \_\ 
                        \/_____/   \/_____/   \/_/  \/_/ 
                                   
                            Undertale Save Manager
                                by wawa | v2.3

    {Fore.LIGHTBLACK_EX}8 - Изменить кол-во убийств  |  9 - Зонт  |  10 - Конец игры?  |  11 - Геноцид?  |  12 - Изменить ID текущей комнаты
    {Fore.LIGHTBLACK_EX}                                             {Fore.LIGHTRED_EX}14 - Редактор инвентаря
    {Style.RESET_ALL} ''')
                print(f"{Fore.GREEN}Предмет {itemedit} помещен в слот {slot}{Style.RESET_ALL}")







    def do_12(self, arg: str):
        directory = pathlib.Path().absolute()
        local = os.getenv('LOCALAPPDATA')
        undertale = 'UNDERTALE'
        print(f'{Fore.LIGHTBLACK_EX}{romids}')
        print(f"{Fore.LIGHTYELLOW_EX}Список ID комнат: ^^^{Style.RESET_ALL}")
            # текущий айди комнаты
        with open(os.path.join(local, undertale, 'file0'), 'r+', encoding='utf-8') as a:
            lines = a.readlines()
            content = a.read()
            roomid = lines[547]
            rid = roomid.replace("\n", "")
            print(f"{Fore.LIGHTYELLOW_EX}Текущий ID комнаты: {rid} {Style.RESET_ALL} \n\n", end="")
        roomedit = input(f"{Fore.LIGHTYELLOW_EX}Введите ID комнаты: {Style.RESET_ALL}")
        if not roomedit.isdigit():
            print(f"{Fore.RED}Введите значение цифрами!{Style.RESET_ALL}")
            return
        else:
            if roomedit == "":
                print(f"{Fore.RED}Введите значение!{Style.RESET_ALL}")
                return
            else:
                from os.path import expanduser
                home = expanduser("~")
                config = configparser.ConfigParser()
                config.optionxform = str
                config_file = os.path.join(home, 'AppData', 'Local', undertale, 'undertale.ini')
                config.read(config_file)
                config.set('General', 'Room', f"\"{roomedit}.000000\"")
                with open(config_file, 'w') as configfile:
                    config.write(configfile)
                with open(os.path.join(local, undertale, 'file0'), 'r+', encoding='utf-8') as f:
                    lines = f.readlines()
                    content = f.read()
                    lines[547] = f'{roomedit}\n'
                    f.seek(0)
                    f.writelines(lines)
                    f.truncate()
                with open(os.path.join(local, undertale, 'file9'), 'r+', encoding='utf-8') as f:
                    lines = f.readlines()
                    content = f.read()
                    lines[547] = f'{roomedit}\n'
                    f.seek(0)
                    f.writelines(lines)
                    f.truncate()
                time.sleep(0.1)
                clear_console()
                time.sleep(0.1)
                print(fr'''{Fore.LIGHTYELLOW_EX}{Style.BRIGHT}


                       __  __     ______     __    __    
                      /\ \/\ \   /\  ___\   /\ "-./  \   
                      \ \ \_\ \  \ \___  \  \ \ \-./\ \  
                       \ \_____\  \/\_____\  \ \_\ \ \_\ 
                        \/_____/   \/_____/   \/_/  \/_/ 

                            Undertale Save Manager
                                by wawa | v2.3

    {Fore.LIGHTBLACK_EX}1 - Изменить FUN  |  2 - Изменить кол-во золота  |  3 - Изменить LV  |  4 - Изменить HP  |  5 - Изменить Имя
    {Fore.LIGHTBLACK_EX}                      6 - Изменить кол-во опыта  |  7 - Далее..
    {Style.RESET_ALL} ''')
                print(f"{Fore.GREEN}ID комнаты изменено на {Fore.LIGHTYELLOW_EX}{roomedit}{Style.RESET_ALL}")

if __name__ == '__main__':
    app = Console()
    app.cmdloop(intro=app.wlauncher)