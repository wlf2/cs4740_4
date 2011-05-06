#!/usr/bin/env python

import re

def get_patterns():
	patternList=[(201,'Leonov'),
	(202,'Central\s+American?'),
	(202,'Yucatan'),
	(202,'neighbou?ring Guatemala'),
	(202,'Guatemala.*border'),
	(202,'boundaries.*Guatemalan?'),
	(202,'Gulf of Honduras.*border(ed)?'),
	(202,'Honduras.*next\s+door'),
	(202,'on a line between Colombia and the US'),
	(203,'400\s+micrograms'),
	(204,'suspension'),
	(204,'supported\s+by\s+cables'),
	(204,'sling'),
	(205,'245,?000'),
	(206,'2[345]0,?000\s+miles'),
	(206,'221,?000\s+miles'),
	(206,'238,?855\s+miles'),
	(207,'national\s+anthem'),
	(207,'Star\s*-?\s*Spangled\s+Banner'),
	(207,'ode\s+to\s+Old\s+Glory'),
	(208,'California'),
	(209,'Johan\s+Vaaler\'?s?'),
	(210,'least\s+five'),
	(210,'nine\s+dogs?'),
	(210,'((11)|(12)|(13)|(14)|(15)|(16)|(17)|(18))((\s*to\s+20)|(\s+dogs?))'),
	(211,'ancient\s+Roman'),
	(212,'Adolph\s+Rickenbacker'),
	(213,'bats?'),
	(214,'20'),
	(215,'Gandhi'),
	(215,'Rao'),
	(215,'Nehru'),
	(215,'Singh'),
	(216,'English'),
	(217,'(mature|aging)\s+trees?'),
	(217,'meadows?'),
	(217,'woods'),
	(217,'scrub'),
	(217,'oak\s+trees?'),
	(217,'hardwood'),
	(218,'zipper'),
	(219,'12[0234]\s+million'),
	(219,'123,622,541|123,150,000'),
	(219,'122.6'),
	(219,'123.3'),
	(219,'122.74?\s+million'),
	(220,'Hawke?'),
	(220,'Keating'),
	(221,'Ray'),
	(222,'Egyptian\s*god'),
	(222,'row.*underworld'),
	(223,'Yugoslav(ia)?'),
	(223,'borders?.*Serbia'),
	(224,'light\s+amplification'),
	(225,'Poseidon'),
	(226,'Hungary|Hungarians?'),
	(226,'Czechoslovakian?'),
	(226,'Austrian?'),
	(226,'Slovak(ia)?'),
	(226,'Allmendingen'),
	(226,'Bratislava'),
	(226,'Romanian?'),
	(226,'Gabcikovo'),
	(226,'Ostrov'),
	(226,'Rye Island'),
	(226,'Bulgarian?'),
	(226,'Serbia'),
	(226,'Ukraine'),
	(226,'Vidin'),
	(226,'Ruse'),
	(226,'Vienna'),
	(226,'Belgrade'),
	(226,'Budapest'),
	(226,'Europe'),
	(226,'Esztergom'),
	(227,'temperature\s+at\s+which\s+moisture\s+would\s*start\s+to\s+condense'),
	(227,'moist\s+air\s+and\s+chill'),
	(227,'in\s+the\s+air'),
	(228,'metals?'),
	(229,'Rozsa'),
	(229,'Gillingham'),
	(229,'Evans'),
	(229,'Sieben'),
	(229,'Oppel'),
	(229,'Barrowman'),
	(229,'Mitchell'),
	(229,'Wharton'),
	(229,'Sanders'),
	(229,'Meagher'),
	(229,'Jager'),
	(229,'Salnikov'),
	(229,'Biondi'),
	(229,'Stewart'),
	(229,'Morale'),
	(229,'Ball'),
	(229,'Gross'),
	(230,'1944'),
	(231,'Petain'),
	(231,'Laval'),
	(232,'Jenkins'),
	(232,'Zworykin'),
	(232,'Parker'),
	(232,'Farnsworth'),
	(233,'Wrights?'),
	(233,'Whitehead'),
	(234,'Whitehead'),
	(234,'Wrights?'),
	(235,'12'),
	(236,'Francisco\s+Vasquez\s+de\s+Coronado'),
	(236,'Coronado\s+Trail\s+Association'),
	(236,'bantamweight'),
	(236,'Celestino\s+Coronado'),
	(236,'Gabriel\s+Coronado'),
	(236,'Elaine\s+Coronado'),
	(236,'exploration'),
	(236,'leader.*gang'),
	(237,'Brahma'),
	(237,'Shiva'),
	(237,'Vishnu'),
	(238,'Organi[s|z]ation\s*of\s*American\s*States?'),
	(239,'Rep'),
	(239,'Representative'),
	(239,'congresswoman'),
	(239,'congress.*seat'),
	(239,'member.*Congress'),
	(240,'(75)|(76)|(78)'),
	(240,'Seventy\s*-?\s*seven'),
	(241,'craters?'),
	(241,'lava\s+lake'),
	(242,'Alamo'),
	(242,'San Jacinto'),
	(243,'Portugal'),
	(244,'Doubleday'),
	(245,'Carolinas?'),
	(245,'N\.C\.?'),
	(246,'sea\s*route\s*around\s*Africa'),
	(246,'sea\s+route.*India'),
	(246,'sail.*India'),
	(247,'North'),
	(247,'Union'),
	(248,'reticulated?\s+pythons?'),
	(249,'Egypt'),
	(249,'Luxor'),
	(250,'Yucatan'),
	(250,'Mexico'),
	(250,'Guatemala'),
	(250,'Punta\s+de\s+Chimino'),
	(250,'Huehuetenango'),
	(250,'Central\s+American\s+countries'),
	(250,'Belize\s+City'),
	(250,'British\s+Honduras'),
	(250,'El\s+Salvador'),
	(250,'Tikal'),
	(251,'12\s+million'),
	(252,'1775'),
	(253,'poets?'),
	(253,'wrote.*lines'),
	(253,'wrote.*poems?'),
	(253,'long\s+poems'),
	(253,'poetical'),
	(253,'poetry'),
	(253,'Immortality\s+Ode'),
	(254,'quail'),
	(255,'Diamond\s+Bar\s+consultant'),
	(256,'Cheops'),
	(256,'Khufu'),
	(257,'plankton'),
	(257,'krill'),
	(257,'herring'),
	(257,'shrimp-like\s+crustaceans'),
	(257,'penguin\s+milkshakes'),
	(258,'water.*cooler'),
	(258,'crevices?'),
	(258,'water.*full\s+of.*fish'),
	(259,'dinosaurs?'),
	(260,'North\s+American?\s+Free\s+Trade\s+Association'),
	(260,'North\s+American?\s+Free\s+Trade\s+Agreement'),
	(261,'Hallmark'),
	(262,'Tokugawas?'),
	(263,'1895'),
	(263,'95\s+years\s+ago'),
	(264,'Robert\s+B\.?\s*Thomas'),
	(265,'pluto'),
	(266,'Greek'),
	(267,'rain\s+clouds'),
	(267,'cumulonimbus'),
	(268,'Brutus'),
	(269,'towering\s+figure\s+of\s+art'),
	(269,'painters?'),
	(269,'artists?'),
	(269,'sculpters?'),
	(269,'self\s*-\s*portrait'),
	(269,'20th\s+century\s+masters?'),
	(269,'Picasso\s+oils?'),
	(269,'Impressionist'),
	(269,'Au\s+Lapin\s+Agile'),
	(269,'Yo\s+Picasso'),
	(269,'harlequin'),
	(269,'rose\s+period'),
	(269,'blue\s+period'),
	(270,'Brazil'),
	(270,'Venezuela'),
	(270,'Colombia'),
	(271,'16\s+to\s+18\s+feet'),
	(271,'1[678]\s*-?\s*foot'),
	(271,'6\s*feet'),
	(272,'Australian?s?'),
	(272,'New\s+Zealand'),
	(272,'Queensland'),
	(272,'Taiwan'),
	(272,'Alaska'),
	(272,'Northern\s+Territory'),
	(272,'Outback'),
	(273,'Nixon'),
	(274,'Butts'),
	(275,'nine\s+million'),
	(275,'16\s+million'),
	(276,'\$\s*24\.64\s*billion'),
	(276,'\$\s*3[01]\s*billion'),
	(276,'\$\s*25\s*billion'),
	(276,'Dollars\s+30\s*billion'),
	(276,'Dollars\s+37\s*bn'),
	(276,'billions.*Sultan.*\$31.0'),
	(277,'5,079,385'),
	(277,'5.1m'),
	(278,'(200)|(169)|(227)|(268)|(338)|(341)'),
	(279,'psychoanalyst'),
	(279,'French\s+analysts?'),
	(279,'Jacques\s+Lacan'),
	(279,'Lacan\s*\'\s*s\s+writings?'),
	(279,'writings?.*Lacan'),
	(279,'Freud\s*,?\s*Jung\s*,?\s*Lacan'),
	(279,'Baudrillard\s*,?\s*Habermas\s*,?\s*Lacan\s*,?\s*CS\s*Lewis'),
	(279,'Lacan\s*,?\s*CS\s*Lewis\s*,?\s*le Corbusier\s*,?\s*McLuhan'),
	(279,'implicated\s+Patrice\s+Pelat'),
	(279,'investiga.*Pechiney\s*aluminium'),
	(279,'found.*La\s+Truffe'),
	(279,'Bas les masques'),
	(279,'editor.*Le\s+Monde'),
	(279,'French\s+journalists?'),
	(279,'Jean\s*-?\s*Francois\s+Lacan'),
	(279,'post\s*-?\s*structuralist'),
	(280,'World\s+Trade\s+(Center|Centre)'),
	(281,'1984'),
	(282,'scale'),
	(282,'plant\s+pests'),
	(282,'leaf-?\s+and\s+flower-?\s*munching\s+pests'),
	(282,'aphids?'),
	(283,'Australia'),
	(283,'outback'),
	(283,'central\s+Australian\s+desert'),
	(284,'age\s*70'),
	(285,'1869'),
	(286,'Keystone'),
	(287,'black\s+South\s+African\s+leaders?'),
	(287,'Archi?bish?op'),
	(287,'bishop'),
	(287,'Nobel\s+Peace'),
	(287,'Nobel\s+prize'),
	(287,'Nobel\s+laureates?'),
	(287,'lead.*Anglican\s+Church'),
	(287,'anti\s*-?\s*apartheid\s+cleric'),
	(287,'anti\s*-?\s*apartheid\s+leader'),
	(288,'1[89]0\s+mph'),
	(289,'orators'),
	(289,'senators'),
	(289,'Sens\.'),
	(289,'statesmen'),
	(289,'Webster\s*\'?\s*s\s+contemporaries'),
	(289,'historic\s+figures'),
	(289,'historical\s+allies'),
	(289,'leading\s+political\s+figures'),
	(289,'legislators'),
	(290,'1989'),
	(291,'8th'),
	(292,'1m\s+square\s+miles'),
	(293,'Capt.*Cook'),
	(293,'Polynesians?'),
	(294,'Sultan.*Brunei'),
	(294,'Tsutsumi'),
	(294,'Hassanal'),
	(294,'Taikichiro\s+Mori'),
	(295,'50'),
	(296,'(\$|Dollars)\s*3.35'),
	(296,'(\$|Dollars)\s*3.80'),
	(296,'(\$|Dollars)\s*4.25'),
	(297,'plants?'),
	(297,'vegetation'),
	(297,'pine\s+needles'),
	(298,'redwoods?'),
	(299,'29'),
	(299,'30'),
	(299,'43'),
	(300,'blood.*cancer'),
	(300,'cancer.*blood'),
	(300,'bone\s*-?\s*marrow.*cancer'),
	(300,'smoking\s*-?\s*related\s+disease'),
	(300,'white\s+blood'),
	(301,'Paul\s+Brown'),
	(301,'Brown.*Christ\s+Hospital'),
	(301,'coach.*Brown'),
	(301,'1960s.*Brown'),
	(302,'10\s+people'),
	(302,'13\s+Americans'),
	(303,'M[ou]hamm[ae]d'),
	(304,'Texas\s+and\s+other.*states'),
	(304,'Will\s+County'),
	(304,'southwest.*Chicago'),
	(305,'metals?'),
	(305,'metallic\s+(substance)|(element)'),
	(305,'strengthening\s+agent'),
	(305,'alloy\s+in\s+steelmaking'),
	(305,'alloying\s+agent'),
	(306,'desert'),
	(306,'Saudi\s+Arabia'),
	(306,'Kenyan?'),
	(306,'African?'),
	(306,'Uganda'),
	(307,'directors?'),
	(307,'direction'),
	(307,'directed'),
	(307,'directs'),
	(307,'Dead\s+Poet\s*\'?\s*s\s+Society'),
	(308,'714'),
	(309,'William.*Cody'),
	(309,'Buffalo\s+Bill\s*\'?\s*\'?\s+Cody'),
	(309,'Buffalo\s+Bill\s*"\s+Cody'),
	(309,'Bill\s+Cody'),
	(309,'Indian\s+(scout)|(fighter)'),
	(309,'pony\s+express'),
	(309,'produced.*Wild\s+West\s+show'),
	(310,'Burma'),
	(310,'Thai(land)?'),
	(310,'Kanchanaburi'),
	(310,'90\s+miles\s+west.*Bangkok'),
	(311,'^\s*four\s*$'),
	(311,'^\s*4\s*$'),
	(311,'^\s*three\s*$'),
	(311,'^\s*3\s*$'),
	(311,'four.*Super\s+Bowls?'),
	(311,'in\s+four\s+tries'),
	(311,'four\s+of\s+the\s+past\s+nine'),
	(311,'fourth\s+in\s+six\s+years'),
	(311,'three\s+(consecutive\s+)?Super'),
	(311,'third\s+straight\s+Super'),
	(311,'1982\s*,?\s*\'?\s*85\s*,?\s*\'?\s*89.*90'),
	(312,'Olmsted'),
	(313,'Ts.*Ai\s+Lun'),
	(313,'Islamic\s+society'),
	(314,'Furnier'),
	(315,'small.*wings'),
	(315,'wings.*too\s+small'),
	(316,'Caspian'),
	(316,'Javan'),
	(316,'Bali'),
	(316,'Tasmanian'),
	(317,'west\s+of\s+the\s+International\s+Date\s+Line'),
	(317,'western\s+Pacific'),
	(317,'south\s+Pacific'),
	(317,'half\s+a\s+world\s+away\s+from\s+Washington'),
	(317,'south\s+of\s+the\s+Northern\s+Marianas'),
	(317,'1\s*,?\s*500\s+miles\s+east\s+of\s+the\s+Philippines'),
	(317,'U\s*\.?\s*S\s*\.?\s+territory\s+in\s+the\s+Pacific'),
	(318,'Harvard'),
	(319,'seven'),
	(319,'7'),
	(320,'Eastern\s+Europe'),
	(320,'central\s+Europe'),
	(320,'southeast\s+Europe'),
	(320,'border.*Hungary'),
	(320,'border.*Yugoslavia'),
	(320,'Rhine\s*-?\s*Main\s*-?\s*Danube\s+trans\s*-?\s*European\s+axis'),
	(320,'Rhine\s*-?\s*Main\s*-?\s*Danube\s+watercourse'),
	(321,'100th\s+anniversary'),
	(321,'1888'),
	(323,'Queen Elizabeth'),
	(323,'Elizabeth II'),
	(323,'the Queen.*richest'),
	(324,'Sacramento'),
	(325,'size.*India'),
	(326,'sea\s*grass'),
	(326,'plant\s*-?\s*eating'),
	(326,'herbivores?'),
	(326,'unwanted\s+vegetation'),
	(326,'lettuce'),
	(327,'82\s+years\s+ago'),
	(327,'1906'),
	(327,'1849'),
	(327,'april\s*18'),
	(327,'\'06'),
	(328,'Hamilton'),
	(329,'80\s+million'),
	(329,'81\s+million'),
	(329,'83\s+million'),
	(329,'85\s+million'),
	(329,'90\s+million'),
	(329,'85\.\s*8\s+million'),
	(329,'86\.\s*7\s+million'),
	(329,'Population\(mn\) 87.8'),
	(330,'1943'),
	(331,'5\s*,?\s*400\s+degrees\s+Fahrenheit'),
	(331,'9\s*,?\s*000\s+degrees\s+Fahrenheit'),
	(331,'5\s*,?\s*000\s+degrees\s+Celsius'),
	(332,'journey.*three\s+years'),
	(332,'about\s+two\s+years'),
	(332,'six\s*-?\s*month.*111\s*million\s*-?\s*mile'),
	(332,'nine\s+months\s+to'),
	(332,'nine\s+month\s+journey'),
	(332,'minimum.*14\s+months?'),
	(332,'flight.*18\s+months?'),
	(332,'240\s+days'),
	(334,'5bn\s+years?'),
	(335,'8.*foot'),
	(335,'9.*feet'),
	(335,'9.*foot'),
	(335,'10.*foot'),
	(335,'10.*feet'),
	(335,'10.*ft'),
	(336,'197[56]'),
	(337,'Dollars?\s*1\s*\.\s*2\s*m'),
	(337,'Pounds?\s*770\s*,?\s*000'),
	(337,'Dollars?\s*1m'),
	(337,'\$\s*5\s*,?\s*800\s+a\s+week'),
	(337,'\$\s*890\s*,?\s*844'),
	(337,'\$\s*800\s*,?\s*000'),
	(337,'\$\s*600\s*,?\s*000'),
	(337,'\$\s*597\s*,?\s*000'),
	(337,'\$\s*586\s*,?\s*816'),
	(337,'\$\s*550\s*,?\s*000'),
	(337,'\$\s*490\s*,?\s*000'),
	(337,'\$\s*412\s*,?\s*520'),
	(337,'\$\s*400\s*,?\s*000'),
	(338,'Naismith'),
	(340,'explorer'),
	(340,'Army\s+lieutenant'),
	(340,'head.*exploratory\s+troop'),
	(340,'Pike\s+sighted'),
	(340,'Pike\s+first\s+saw'),
	(341,'2\s*,?\s*300\s+miles'),
	(341,'2\s*,?\s*500\s+miles'),
	(342,'ben[td]'),
	(342,'separate'),
	(342,'break\s+apart'),
	(342,'split.*light'),
	(342,'refract'),
	(342,'spread'),
	(342,'combines.*single\s+beam'),
	(343,'Amazon.*longest'),
	(343,'longest.*Amazon'),
	(343,'Nile.*longest'),
	(344,'Skinner'),
	(344,'Jung'),
	(344,'Pavlov'),
	(344,'Charles.*Thomas'),
	(344,'Sigmund\s+Freud'),
	(345,'2\s*,?\s*467\s*,?\s*845'),
	(345,'2\s*\.\s*49\s+million'),
	(346,'poets?'),
	(346,'writers?'),
	(346,'poem.*Langston'),
	(346,'Hughes.*poetry'),
	(346,'Hughes.*poems?'),
	(346,'Hughes.*wrote'),
	(346,'poetry.*Hughes'),
	(347,'a\s+Claude\s+Monet\s+impression'),
	(347,'impressionists?'),
	(347,'painting\s+is\s+the\s+stolen\s+Monet'),
	(347,'painter.*Claude\s+Monet'),
	(347,'artists\s+include.*Monet'),
	(347,'painted\s+by\s+Monet?'),
	(347,'Monet\s*\'?\s*s\s+paintings?'),
	(347,'paintings\s+included\s+five\s+Monet\s*\'?\s*s'),
	(347,'Impression Sunrise'),
	(347,'treat\s+art\s+as\s+Monet\s+did'),
	(347,'Monet\s+made\s+his\s+art'),
	(347,'artist\s+of\s+immense\s+wealth'),
	(347,'series.*paintings'),
	(347,'Monet\s+painted'),
	(347,'works?\s+by\s+Monet'),
	(347,'painting\s+at\s+Orsay'),
	(347,'paintings?\s+by\s+(Claude\s+)?Monet'),
	(347,'Nature\s+into\s+Art'),
	(347,'purchaser\s+of\s+the\s+Monet'),
	(347,'Monet.*landscapes?'),
	(347,'landscape.*Monet'),
	(347,'father\s+of\s+impressionism'),
	(348,'Zo[zs]er'),
	(349,'Valley\s+of\s+the\s+Dolls'),
	(349,'The\s+Civil\s+War'),
	(349,'Fatherhood'),
	(349,'Gone\s+with\s+the\s+Wind'),
	(349,'Bible'),
	(350,'1\s*,?\s*116'),
	(350,'nearly\s+1\s*,?\s*120'),
	(350,'650'),
	(351,'pioneering\s+aviator'),
	(351,'aviator.*Lindbergh'),
	(351,'solo.*crossing'),
	(351,'kidnapping.*son'),
	(351,'kidnap.*Lindbergh'),
	(351,'first.*solo.*Atlantic'),
	(351,'first.*cross.*Atlantic'),
	(351,'flight.*Atlantic.*1927'),
	(351,'historic.*Atlantic\s+crossing'),
	(351,'famous\s+solo\s+flight'),
	(351,'flying\s+ace'),
	(351,'hero\s+pilot'),
	(351,'design\s+the\s+pontooned\s+planes'),
	(351,'isolationists?\s+before\s+World\s+War\s+II'),
	(351,'isolationist\s+movement'),
	(352,'Robinson.*McGraw'),
	(352,'Baltimore'),
	(352,'Egyptians'),
	(353,'Hindu-Arabic'),
	(354,'worms?'),
	(354,'Steinernema\s+feltiae'),
	(354,'insects\s*\'?\s+natural\s+enemies'),
	(354,'eelworms?'),
	(354,'roundworms?'),
	(354,'parasitic'),
	(354,'plant\s+parasite'),
	(354,'pinewood\s+nematode'),
	(354,'voracious\s+bug\s+killers'),
	(354,'microscopic\s+organism'),
	(355,'Bugatti\s+Royale'),
	(356,'cocoa\s+bean'),
	(357,'Alaska'),
	(358,'looks\s+like\s+a\s+cross\s+between\s+a\s+dog\s+and\s+a\s+monkey'),
	(358,'rodents?'),
	(358,'mongoose'),
	(359,'Australian?'),
	(359,'Fla\.'),
	(360,'6.2\s*-?\s*miles?'),
	(361,'300\s*degrees\s+Fahrenheit'),
	(361,'1\s*,?\s*800\s*degrees'),
	(361,'1\s*,?\s*000\s*degrees'),
	(362,'Ouagadougo?u'),
	(363,'Port\s*-?\s*au\s*-?\s*Prince'),
	(364,'1\s*,\s*605\s*,?\s*000'),
	(365,'14\.[57]\s*million'),
	(365,'15\)?\s*m(illion)?'),
	(366,'San\s+Francisco'),
	(366,'49\s*ers'),
	(367,'Jan\.\)?\s*15'),
	(367,'January\s+15'),
	(368,'Caribbean'),
	(368,'off.*coast.*Venezuela'),
	(369,'Alaska'),
	(369,'Soviet\s+Inuits?'),
	(369,'Arctic'),
	(369,'Greenland(ers)?'),
	(369,'Canada'),
	(369,'Canadian\s+Inuits?'),
	(369,'Canadian\s+Eskimos?'),
	(369,'Siberian?'),
	(369,'Soviet\s+Union.*Yuit'),
	(369,'Iqaluit'),
	(369,'Nunavut'),
	(369,'Ellesmere'),
	(370,'skin'),
	(371,'dogs?'),
	(371,'pooches'),
	(372,'(March\s*25\s*,?\s*)?1911'),
	(373,'Africa'),
	(373,'Botswana'),
	(373,'west\s+of\s+Kariba'),
	(373,'50\s+miles.*Kuruman'),
	(373,'south\s+of\s+Victoria\s+Falls'),
	(374,'ailment'),
	(374,'metabolic\s+disorder'),
	(374,'Poems?'),
	(375,'Atlantic'),
	(376,'Truman'),
	(377,'30\s*km\s*/?\s*sec'),
	(378,'Hirohito'),
	(378,'Akihito'),
	(378,'Showa'),
	(378,'Taisho'),
	(379,'100\s*,?\s*000\s+light\s*-?\s*years?'),
	(380,'Portuguese'),
	(381,'Czolgosz'),
	(382,'7\s*th\s+century'),
	(383,'saguaros?'),
	(383,'pronounced\s+suh-WAH-row'),
	(384,'Marconi'),
	(384,'Lear'),
	(385,'Busch\s+Gardens'),
	(385,'Libya'),
	(385,'Serengeti'),
	(385,'Tanzania'),
	(385,'Kenya'),
	(385,'East\s+Africa\s*\'?\s*s\s+Eden\s*-?\s*like\s+game\s+parks?'),
	(385,'Zimbabwe'),
	(386,'eating\s+disorders?'),
	(386,'condition.*refusal.*eat'),
	(386,'self\s*-?\s*starvation'),
	(386,'an\s+avoidance\s+of\s+food'),
	(386,'aversion\s+to\s+eating'),
	(386,'psychological\s+problems?'),
	(387,'1889'),
	(387,'1989.*hundred.*years.*ago.*Montana'),
	(388,'Nina.*Pinta.*Santa\s+Maria'),
	(388,'Pinta.*Nina.*Santa\s+Maria'),
	(389,'Arthur'),
	(390,'Norfolk\s+County'),
	(390,'Massachusetts'),
	(390,'Braintree\s*,?\s*Mass'),
	(390,'Quincy\s*,?\s*Mass'),
	(390,'Franklin\s+St.*Quincy'),
	(390,'in\s+Braintree'),
	(391,'Manet'),
	(392,'god.*hurricane'),
	(392,'Aztec.*god'),
	(392,'god.*ancient\s+Aztecs'),
	(392,'priest\s*-?\s*leader\s+of\s+Tula'),
	(392,'Toltec\s+god'),
	(392,'brother.*Tezcatlipoca'),
	(392,'the\s+god\s+Quetzalcoatl'),
	(392,'god\s+of\s+learning'),
	(392,'South\s+American\s+Indian.*god'),
	(393,'brain'),
	(394,'floccinaucinihilipilification'),
	(394,'pneumonoultramicroscopicsilicovolcanoconiosis'),
	(395,'ingredient.*gunpowder'),
	(395,'potassium\s+nitrate'),
	(396,'General\s+Electric'),
	(397,'1788'),
	(397,'18th\s+century'),
	(398,'ten\s+days.*January 4'),
	(398,'Christmas.*Boxing Day'),
	(398,'26\s*December'),
	(398,'December\s+26'),
	(398,'day\s+after\s+Christmas'),
	(399,'UK\s*currency.*Dollars\s*1\.4945'),
	(399,'to\s+\$\s*1\.7091'),
	(10000,'Nov\s*9'),
	(10001,'Lou\s+Vasquez'),
	(10002,'spade\s+shaped'),
	(10003,'60\s+million'),
	(10004,'Denmark'),
	(10005,'substantia\s+nigra'),
	(10006,'May\s+18'),
	(10007,'Burgh\s+Island\s+Hotel'),
	(10008,'1215'),
	(10009,'William\s+Seward'),
	(10010,'3\s+1/2\s+hours'),
	(10011,'270'),
	(10012,'5.7bn'),
	(10013,'Brazil'),
	(10014,'Gilbert'),
	(10015,'3\s+hours\s+45\s+minutes'),
	(10016,'Robert\s+Angel'),
	(10017,'2,100\s+miles'),
	(10018,'Little'),
	(10019,'4\s+minutes,\s+43\s+seconds'),
	(10020,'Washington'),
	(10021,'92m'),
	(10022,'Kampala'),
	(10023,'Madison'),
	(10024,'Lansing'),
	(10025,'South\s+America'),
	(10026,'Illinois'),
	(10027,'Monsanto\s+and\s+Eli\s+Lilley'),
	(10028,'Neil\s+Armstrong'),
	(10029,'Sunday,\s+25\s+March\s+1990'),
	(10030,'May\s+6,\s+1994'),
	(10031,'10\s+May\s+1994'),
	(10032,'Saparmurad\s+Niyazov'),
	(10033,'Tchaikovsky'),
	(10034,'about\s+2015\s+or\s+2020'),
	(10035,'Zebra\s+Mussel'),
	(10036,'John\s+F.\s+Welch\s+Jr.'),
	(10037,'1,000\s+foot\s+high')]
	patternDict={}
	for pattern in patternList:
		if pattern[0] in patternDict.keys():
			patternDict[pattern[0]].append(pattern[1])
		else:
			patternDict[pattern[0]]=[pattern[1]]
	return patternDict

#Take True or False and return 1 or -1
def boolto1(boolean):
	if boolean==True:
		return 1
	elif boolean==False:
		return -1
	else:
		return None

def check_answer(q_id,candidate):
	if q_id in patterns.keys():
		pass
	else:
		print 'Invalid question number'
		return False
	def check_one_pattern(one_pattern):
		return re.match(one_pattern,candidate[0])!=None
	return boolto1(reduce(lambda a,b: ( a or check_one_pattern(b) ) , patterns[q_id],False))

patterns=get_patterns()

if __name__ == '__main__':
	candidate=('California','taoseutasoetuh08',1438,'NNP')
	print check_answer(10008,candidate)