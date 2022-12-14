from random import randint


def fact():
    facts = ['Самая крупная жемчужина в мире достигает 6 килограммов в весе.',
             'Законодательство США допускало отправку детей по почте до 1913 года.',
             'В языке древних греков не существовало слова, которое обозначало религию.,',
             'В современной истории есть промежуток времени, когда на счетах компании «Apple», было больше средств, чем у американского правительства.',
             'Среднее облако весит порядка 500 тонн, столько же весят 80 слонов.',
             'В Ирландии никогда не было кротов.'
             'До 7 месяцев ребенок может дышать и глотать одновременно.'
             'Емкость мозга человека превышает 4 терабайта.'
             'Люди - единственные существа, которые спят на спине.',
             'Флот США содержит больше авианосцев, чем все флоты мира вместе взятые.',
             'Скорость распространения лавы после извержения, близка к скорости бега гончей.',
             'Изначально, отвертка была изобретена для выковыривания гвоздей, шуруп был изобретен на 100 лет позже.',
             'Библия – книга, которую чаще всего воруют в американских магазинах.',
             'Примерно 1/3 всей соли, производимой в США, расходуется на очистку дорог ото льда.',
             'Существует пробирка, диаметр которой, в 10000 раз меньше диаметра человеческого волоса.',
             'Саудовская Аравия не содержит рек.',
             'В Антарктиде существует единственная река – Оникс, она течет всего 60 дней в году.',
             'У медуз нет мозгов и кровеносных сосудов.',
             'Ежедневно 60 человек становятся миллионерами.',
             'До 17 века термометры заполняли коньяком.',
             'Кошки спят больше половины своей жизни.',
             'Лимон содержит больше сахара, чем клубника.',
             'Самый долгий полёт курицы продолжался 13 секунд.',
             'Ладожское озеро является самым большим в Европе.',
             'За год на Землю падает до 500 кг марсианского метеорита.',
             'Земля делает полный оборот вокруг своей оси за 23 часа 56 минут и 4 секунды.',
             'На Юпитере регулярно идут алмазные дожди.']

    return facts[randint(0, len(facts) - 1)]


def joke():
    joke_data = ['— Зачем последним моделям Лэнд Ровер обогрев заднего стекла?\n'
                 '— Чтобы руки не мёрзли, когда толкаете его в сервис…'
                 '– Если RangRover проехал мимо автосервиса – то значит у него отказали тормоза 😀',
                 '-Ленд Роверы покупают по два в одни руки: пока один в сервисе, на втором поездить можно.\n'
                 ' -Потом наоборот',
                 '-А знаете почему у лэндроверов самый низкий расход топлива?\n'
                 '-потому-что их обычно буксируют, так как они сломались…'
                 '-Почему не здороваются владельцы LR — они уже виделись с утра на сервисе', ]
    return joke_data[randint(0, len(joke_data) - 1)]
