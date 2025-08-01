def translate(language, code):
    try:
        return LANG[code][language]
    except:
        return code

LANG = {
    'room_already_exists':
        {
            'en': 'Room already exists',
            'vi': 'Phòng đã tồn tại'
        },
    'Room_information_updated':
        {
            'en': 'Room information updated',
            'vi': 'Thông tin phòng đã được cập nhật'
        },
    'usdt_is_not_enough':
        {
            'en': 'Balance is not enough',
            'vi': 'Số dư tài khoản không đủ'
        },
    'MKT_accounts_are_not_accepted':
        {
            'en': 'MKT accounts are not accepted.',
            'vi': 'Tài khoản MKT không được chấp nhận.'
        },
    'VIP_level_must_be_level_3_or_higher':
        {
            'en': 'VIP level must be level 3 or higher',
            'vi': 'Cấp độ VIP phải là cấp độ 3 trở lên'
        },
    'Minimum_deposit_of_100':
        {
            'en': 'Minimum deposit of $100',
            'vi': 'Ký quỹ tối thiểu $100'
        },
    'Roll_you_win':{
        'en': 'You win ${}<br>{} lottery tickets, {} exp',
        'vi': 'Bạn thắng ${}<br>{} vé số, {} exp'
    }
}
# {{ LANG['choose_account'][user_language] }}
WEB_LANGUAGE = {
    'welcome': {
        'en': 'WELCOME',
        'vi': 'XIN CHÀO',
        'ru': 'Добро пожаловать',  #nga
        'fr': 'Bienvenue',  # french
        'hi': 'स्वागत'  #indi
    },
    'choose_account': {
        'en': 'Choose account',
        'vi': 'Chọn tài khoản',
        'ru': 'Выберите аккаунт',
        'fr': 'Choisir un compte',
        'hi': 'खाता चुनें'
    },
    'account': {
        'en': 'Account',
        'vi': 'Tài khoản',
        'ru': 'Аккаунт',
        'fr': 'Compte',
        'hi': 'खाता'
    },
    'forward': {
        'en': 'Forward',
        'vi': 'Chuyển tiếp',
        'ru': 'Переслать',
        'fr': 'Transférer',
        'hi': 'आगे भेजें'
    },
    'go_to_claim_page': {
        'en': 'Go to the free USDT claim page',
        'vi': 'Chuyển đến trang nhận miễn phí USDT',
        'ru': 'Перейти на страницу получения бесплатных USDT',
        'fr': 'Aller à la page de réception gratuite de USDT',
        'hi': 'मुफ़्त USDT प्राप्त करने वाले पेज पर जाएँ'
    },
    'claim_free': {
        'en': 'Claim Free',
        'vi': 'NHẬN MIỄN PHÍ',
        'ru': 'Получить бесплатно',
        'fr': 'Recevoir gratuitement',
        'hi': 'मुफ़्त प्राप्त करें'
    },
    'invest': {
        'en': 'Invest',
        'vi': 'ĐẦU TƯ',
        'ru': 'Инвестиции',
        'fr': 'Investir',
        'hi': 'निवेश'
    },
    'wallet_management': {
        'en': 'Wallet Management',
        'vi': 'QUẢN LÝ VÍ',
        'ru': 'Управление кошельком',
        'fr': 'Gestion de portefeuille',
        'hi': 'वॉलेट प्रबंधन'
    },
    'marketing': {
        'en': 'Marketing',
        'vi': 'Tiếp thị',
        'ru': 'Маркетинг',
        'fr': 'Marketing',
        'hi': 'विपणन'
    },
    'support': {
        'en': 'Support',
        'vi': 'Hỗ trợ',
        'ru': 'Поддержка',
        'fr': 'Assistance',
        'hi': 'सहायता'
    },
    'get_free': {
        'en': 'Get Free',
        'vi': 'Nhận miễn phí',
        'ru': 'Получить бесплатно',
        'fr': 'Obtenir gratuitement',
        'hi': 'मुफ़्त प्राप्त करें'
    },
    'free': {
        'en': 'Free',
        'vi': 'Miễn phí',
        'ru': 'Бесплатно',
        'fr': 'Gratuit',
        'hi': 'मुफ़्त'
    },
    'weekly_lottery': {
        'en': 'Weekly Lottery',
        'vi': 'Xổ số tuần',
        'ru': 'Еженедельная лотерея',
        'fr': 'Loterie hebdomadaire',
        'hi': 'साप्ताहिक लॉटरी'
    },
    'lucky_number': {
        'en': 'Lucky Number',
        'vi': 'Số may mắn',
        'ru': 'Счастливое число',
        'fr': 'Numéro chanceux',
        'hi': 'शुभ अंक'
    },
    'payout': {
        'en': 'Payout',
        'vi': 'Chi trả',
        'ru': 'Выплата',
        'fr': 'Paiement',
        'hi': 'भुगतान'
    },
    'roll': {
        'en': 'Roll',
        'vi': 'Quay',
        'ru': 'Крутить',
        'fr': 'Lancer',
        'hi': 'घुमाएँ'
    },
    'history': {
        'en': 'History',
        'vi': 'LỊCH SỬ',
        'ru': 'История',
        'fr': 'Historique',
        'hi': 'इतिहास'
    },
    'day': {
        'en': 'Day',
        'vi': 'Ngày',
        'ru': 'День',
        'fr': 'Jour',
        'hi': 'दिन'
    },
    'receive': {
        'en': 'Receive',
        'vi': 'Nhận',
        'ru': 'Получить',
        'fr': 'Recevoir',
        'hi': 'प्राप्त करें'
    },
    'no_history': {
        'en': 'No history yet',
        'vi': 'Chưa có lịch sử',
        'ru': 'История отсутствует',
        'fr': 'Aucun historique pour le moment',
        'hi': 'अभी तक कोई इतिहास नहीं है'
    },
    'lottery_round': {
        'en': 'Lottery Round',
        'vi': 'Kỳ xổ số',
        'ru': 'Раунд лотереи',
        'fr': 'Tour de loterie',
        'hi': 'लॉटरी राउंड'
    },
    'ends_in': {
        'en': 'Ends in',
        'vi': 'Kết thúc sau',
        'ru': 'Заканчивается через',
        'fr': 'Se termine dans',
        'hi': 'समाप्त होता है'
    },
    'days': {
        'en': 'Days',
        'vi': 'Ngày',
        'ru': 'Дни',
        'fr': 'Jours',
        'hi': 'दिन'
    },
    'hours': {
        'en': 'Hours',
        'vi': 'Giờ',
        'ru': 'Часы',
        'fr': 'Heures',
        'hi': 'घंटे'
    },
    'minutes': {
        'en': 'Minutes',
        'vi': 'Phút',
        'ru': 'Минуты',
        'fr': 'Minutes',
        'hi': 'मिनट'
    },
    'seconds': {
        'en': 'Seconds',
        'vi': 'Giây',
        'ru': 'Секунды',
        'fr': 'Secondes',
        'hi': 'सेकंड'
    },
    'your_tickets': {
        'en': 'YOUR TICKETS',
        'vi': 'VÉ CỦA BẠN',
        'ru': 'ВАШИ БИЛЕТЫ',
        'fr': 'VOS BILLETS',
        'hi': 'आपके टिकट'
    },
    'total_tickets': {
        'en': 'TOTAL TICKETS',
        'vi': 'TỔNG SỐ VÉ',
        'ru': 'ВСЕГО БИЛЕТОВ',
        'fr': 'NOMBRE TOTAL DE BILLETS',
        'hi': 'कुल टिकट'
    },
    'win_chance': {
        'en': 'WIN CHANCE',
        'vi': 'CƠ HỘI THẮNG',
        'ru': 'ШАНС НА ПОБЕДУ',
        'fr': 'CHANCE DE GAGNER',
        'hi': 'जीतने का मौका'
    },
    'buy_tickets': {
        'en': 'BUY TICKETS',
        'vi': 'MUA VÉ',
        'ru': 'КУПИТЬ БИЛЕТЫ',
        'fr': 'ACHETER DES BILLETS',
        'hi': 'टिकट खरीदें'
    },
    'number_of_tickets': {
        'en': 'NO. OF TICKETS',
        'vi': 'SỐ LƯỢNG VÉ',
        'ru': 'КОЛ-ВО БИЛЕТОВ',
        'fr': 'NOMBRE DE BILLETS',
        'hi': 'टिकटों की संख्या'
    },
    'enter_number_of_tickets': {
        'en': 'Enter no. of tickets',
        'vi': 'Nhập số lượng vé',
        'ru': 'Введите кол-во билетов',
        'fr': 'Entrez le nombre de billets',
        'hi': 'टिकटों की संख्या दर्ज करें'
    },
    'price_per_ticket': {
        'en': 'PRICE PER TICKET',
        'vi': 'GIÁ MỖI VÉ',
        'ru': 'ЦЕНА ЗА БИЛЕТ',
        'fr': 'PRIX PAR BILLET',
        'hi': 'प्रति टिकट मूल्य'
    },
    'total_amount': {
        'en': 'TOTAL AMOUNT',
        'vi': 'TỔNG SỐ TIỀN',
        'ru': 'ОБЩАЯ СУММА',
        'fr': 'MONTANT TOTAL',
        'hi': 'कुल राशि'
    },
    'buy': {
        'en': 'BUY',
        'vi': 'MUA',
        'ru': 'КУПИТЬ',
        'fr': 'ACHETER',
        'hi': 'खरीदें'
    },
    'previous_win': {
        'en': 'PREVIOUS WIN',
        'vi': 'CHIẾN THẮNG KỲ TRƯỚC',
        'ru': 'ПРЕДЫДУЩИЙ ВЫИГРЫШ',
        'fr': 'GAIN PRÉCÉDENT',
        'hi': 'पिछली जीत'
    },
    'tickets': {
        'en': 'Tickets',
        'vi': 'Vé',
        'ru': 'Билеты',
        'fr': 'Billets',
        'hi': 'टिकट'
    },
    'pay_confirm': {
        'en': 'Confirm Payment',
        'vi': 'Xác nhận thanh toán',
        'ru': 'Подтвердить оплату',
        'fr': 'Confirmer le paiement',
        'hi': 'भुगतान की पुष्टि करें'
    },
    'confirm_your_pay': {
        'en': 'Confirm your pay!',
        'vi': 'Xác nhận thanh toán của bạn!',
        'ru': 'Подтвердите свой платёж!',
        'fr': 'Confirmez votre paiement !',
        'hi': 'अपना भुगतान पुष्टि करें!'
    },
    'buy_n_tickets': {
        'en': 'Buy {n} tickets',
        'vi': 'Mua {n} vé',
        'ru': 'Купить {n} билетов',
        'fr': 'Acheter {n} billets',
        'hi': '{n} टिकट खरीदें'
    },
    'game': {
        'en': 'GAME',
        'vi': 'TRÒ CHƠI',
        'ru': 'ИГРА',
        'fr': 'JEU',
        'hi': 'खेल'
    },
    'transaction': {
        'vi': 'Giao dịch',
        'en': 'Transaction',
        'ru': 'Транзакция',
        'fr': 'Transaction',
        'hi': 'लेनदेन'
    },
    'direct_subordinate': {
        'en': 'Direct Subordinate',
        'vi': 'Cấp dưới trực tiếp',
        'ru': 'Прямой подчинённый',
        'fr': 'Subordonné direct',
        'hi': 'प्रत्यक्ष अधीनस्थ'
    },
    'indirect_subordinate': {
        'en': 'Team’s Downline',
        'vi': 'Cấp dưới của đội',
        'ru': 'Участник команды',
        'fr': 'Sous-membre de l’équipe',
        'hi': 'टीम के अधीनस्थ'
    },
    'number_of_registrants': {
        'en': 'Number of Registrants',
        'vi': 'Số người đăng ký',
        'ru': 'Количество зарегистрированных',
        'fr': 'Nombre d’inscrits',
        'hi': 'पंजीकृत लोगों की संख्या'
    },
    'accumulated_balance': {
        'en': 'Accumulated Balance',
        'vi': 'Số dư tích luỹ',
        'ru': 'Накопленный баланс',
        'fr': 'Solde accumulé',
        'hi': 'संचित शेष राशि'
    },
    'first_package_users': {
        'en': 'Users registered for the first package',
        'vi': 'Số người đăng ký gói đầu',
        'ru': 'Пользователи, зарегистрировавшие первый пакет',
        'fr': 'Utilisateurs inscrits au premier forfait',
        'hi': 'पहले पैकेज के लिए पंजीकृत उपयोगकर्ता'
    },
    'referral_link': {
        'en': 'Referral Link',
        'vi': 'LINK GIỚI THIỆU',
        'ru': 'Реферальная ссылка',
        'fr': 'Lien de parrainage',
        'hi': 'रेफ़रल लिंक'
    },
    'enter_referral_code': {
        'en': 'Enter Referral Code',
        'vi': 'Nhập Mã giới thiệu',
        'ru': 'Введите реферальный код',
        'fr': 'Entrez le code de parrainage',
        'hi': 'रेफ़रल कोड दर्ज करें'
    },
    'sign_up': {
        'en': 'Sign Up',
        'vi': 'ĐĂNG KÝ',
        'ru': 'Зарегистрироваться',
        'fr': 'S’inscrire',
        'hi': 'पंजीकरण करें'
    },
    'copy_invite_code': {
        'en': 'Copy Invitation Code',
        'vi': 'Sao chép mã mời',
        'ru': 'Скопировать код приглашения',
        'fr': 'Copier le code d’invitation',
        'hi': 'आमंत्रण कोड कॉपी करें'
    },
    'subordinate_data': {
        'en': 'Subordinate Data',
        'vi': 'Dữ liệu cấp dưới',
        'ru': 'Данные подчинённых',
        'fr': 'Données des subordonnés',
        'hi': 'अधीनस्थ डेटा'
    },
    'commission_details': {
        'en': 'Commission Details',
        'vi': 'Chi tiết hoa hồng',
        'ru': 'Детали комиссии',
        'fr': 'Détails de la commission',
        'hi': 'कमीशन विवरण'
    },
    'invitation_rules': {
        'en': 'Invitation Rules',
        'vi': 'Quy tắc mời',
        'ru': 'Правила приглашения',
        'fr': 'Règles d’invitation',
        'hi': 'निमंत्रण नियम'
    },
    'commission_history': {
        'en': 'Commission History',
        'vi': 'Lịch sử hoa hồng',
        'ru': 'История комиссий',
        'fr': 'Historique des commissions',
        'hi': 'कमीशन इतिहास'
    },
    'support_24_7': {
        'en': '24/7 Support',
        'vi': 'Hỗ trợ 24h/7',
        'ru': 'Поддержка 24/7',
        'fr': 'Assistance 24h/7j',
        'hi': '24/7 सहायता'
    },
    'subordinate_data_upper': {
        'en': 'SUBORDINATE DATA',
        'vi': 'DỮ LIỆU CẤP DƯỚI',
        'ru': 'ДАННЫЕ ПОДЧИНЁННЫХ',
        'fr': 'DONNÉES DES SUBORDONNÉS',
        'hi': 'अधीनस्थ डेटा'
    },
    'commission_details_upper': {
        'en': 'COMMISSION DETAILS',
        'vi': 'CHI TIẾT HOA HỒNG',
        'ru': 'ПОДРОБНОСТИ КОМИССИИ',
        'fr': 'DÉTAILS DES COMMISSIONS',
        'hi': 'कमीशन विवरण'
    },
    'game_commission_structure': {
        'en': 'GAME COMMISSION (3 levels, 8 ranks)',
        'vi': 'HOA HỒNG TRÒ CHƠI (3 tầng, 8 bậc)',
        'ru': 'ИГРОВАЯ КОМИССИЯ (3 уровней, 8 званий)',
        'fr': 'COMMISSION DE JEU (3 niveaux, 8 rangs)',
        'hi': 'गेम कमीशन (3 स्तर, 8 रैंक)'
    },
    'rank': {
        'en': 'RANK',
        'vi': 'BẬC',
        'ru': 'РАНГ',
        'fr': 'RANG',
        'hi': 'रैंक'
    },
    'investment_commission_structure': {
        'en': 'INVESTMENT COMMISSION (3 levels, 8 ranks)',
        'vi': 'HOA HỒNG ĐẦU TƯ (3 tầng, 8 bậc)',
        'ru': 'ИНВЕСТИЦИОННАЯ КОМИССИЯ (3 уровней, 8 званий)',
        'fr': 'COMMISSION D\'INVESTISSEMENT (3 niveaux, 8 rangs)',
        'hi': 'निवेश कमीशन (3 स्तर, 8 रैंक)'
    },
    'invitation_explanation_1': {
        'vi': 'Việc mời bạn được chia thành 8 cấp độ, nếu a mời b thì b là bạn cấp 1 của a. nếu b mời c thì c là bạn cấp 1 của b và cũng là bạn cấp 2 của a. nếu c mời d thì d thuộc bạn cấp 1 của c, đồng thời thuộc bạn cấp 2 của b, đồng thời là bạn cấp 3 của a.',
        'en': 'Inviting friends is divided into 8 levels. If A invites B, then B is level-1 friend of A. If B invites C, then C is B’s level-1 friend and also A’s level-2 friend. If C invites D, then D is level-1 for C, level-2 for B, and level-3 for A.',
        'ru': 'Приглашения делятся на 8 уровней. Если A приглашает B, то B — друг первого уровня для A. Если B приглашает C, то C — друг первого уровня для B и второго уровня для A. Если C приглашает D, то D — первый уровень для C, второй для B и третий для A.',
        'fr': 'Les invitations sont réparties en 8 niveaux. Si A invite B, alors B est un ami de niveau 1 de A. Si B invite C, alors C est un ami de niveau 1 de B et de niveau 2 de A. Si C invite D, alors D est de niveau 1 pour C, de niveau 2 pour B, et de niveau 3 pour A.',
        'hi': 'मित्रों को आमंत्रित करना 8 स्तरों में बाँटा गया है। यदि A, B को आमंत्रित करता है, तो B A का स्तर 1 मित्र है। यदि B, C को आमंत्रित करता है, तो C, B का स्तर 1 मित्र और A का स्तर 2 मित्र है। यदि C, D को आमंत्रित करता है, तो D C का स्तर 1, B का स्तर 2 और A का स्तर 3 मित्र होगा।'
    },
    'invitation_explanation_2': {
        'vi': 'Khi khuyến khích một người bạn đăng ký, bạn cần chuyển liên kết do người mời cung cấp hoặc nhập mã mời của người mời theo cách thủ công để trở thành bạn cấp 1 của người mời.',
        'en': 'To invite a friend to register, you must send them the inviter\'s link or have them manually enter the inviter\'s referral code to become their level-1 friend.',
        'ru': 'Чтобы пригласить друга зарегистрироваться, нужно отправить ему ссылку пригласившего или ввести пригласительный код вручную, чтобы стать другом первого уровня.',
        'fr': 'Pour inviter un ami à s’inscrire, vous devez lui transmettre le lien de parrainage ou entrer manuellement son code d’invitation pour devenir un ami de niveau 1.',
        'hi': 'किसी मित्र को पंजीकरण के लिए आमंत्रित करने के लिए, आपको उन्हें आमंत्रक का लिंक भेजना होगा या आमंत्रण कोड मैन्युअल रूप से दर्ज करना होगा ताकि वे आमंत्रक के स्तर 1 मित्र बन सकें।'
    },
    'invitation_explanation_3': {
        'vi': 'Người được mời đăng ký thông qua mã mời của người mời thì hoa hồng có hiệu lực ngay',
        'en': 'If the invitee registers using the inviter\'s referral code, the commission takes effect immediately.',
        'ru': 'Если приглашённый регистрируется с кодом приглашения, комиссия вступает в силу немедленно.',
        'fr': 'Si l’invité s’inscrit avec le code d’invitation du parrain, la commission prend effet immédiatement.',
        'hi': 'यदि आमंत्रित व्यक्ति आमंत्रक का रेफ़रल कोड उपयोग करके पंजीकरण करता है, तो कमीशन तुरंत प्रभावी हो जाता है।'
    },
    'invitation_explanation_4': {
        'vi': 'Việc tính hoa hồng được xử lý ngay lập tức khi giao dịch hoàn tất và hoa hồng sẽ được thưởng vào ví, bạn có thể vào xem lịch sử hoa hồng để nhận.',
        'en': 'Commission is processed immediately after the transaction is completed and will be credited to your wallet. You can check the commission history to claim it.',
        'ru': 'Комиссия рассчитывается сразу после завершения транзакции и зачисляется в ваш кошелёк. Вы можете просмотреть историю комиссий, чтобы её получить.',
        'fr': 'La commission est traitée immédiatement après la finalisation de la transaction et sera créditée sur votre portefeuille. Vous pouvez consulter l’historique des commissions pour la recevoir.',
        'hi': 'लेन-देन पूरा होने के बाद कमीशन तुरंत संसाधित होता है और आपके वॉलेट में जोड़ दिया जाता है। आप इसे प्राप्त करने के लिए कमीशन इतिहास देख सकते हैं।'
    },
    'invitation_explanation_5': {
        'vi': 'Tùy theo mức hoàn trả mà tỷ lệ hoàn trả được hưởng là khác nhau.',
        'en': 'The rebate rate varies depending on the rebate level.',
        'ru': 'Ставка возврата зависит от уровня возврата.',
        'fr': 'Le taux de remboursement varie en fonction du niveau de remboursement.',
        'hi': 'रिबेट स्तर के अनुसार रिबेट दर भिन्न होती है।'
    },
    'invitation_explanation_6': {
        'vi': 'Số lượng Đội: Số thành viên trong đội có giao dịch trong tuần.',
        'en': 'Team Count: Number of team members who made transactions this week.',
        'ru': 'Количество команды: Число участников команды, совершивших транзакции на этой неделе.',
        'fr': 'Nombre d\'équipe : Nombre de membres de l\'équipe ayant effectué des transactions cette semaine.',
        'hi': 'टीम की संख्या: इस सप्ताह लेनदेन करने वाले टीम सदस्यों की संख्या।'
    },
    'invitation_explanation_7': {
        'vi': 'Cược theo đội: Tổng số lần đặt cược của cấp dưới của bạn trong một tuần.',
        'en': 'Team Bets: Total number of bets placed by your subordinates in one week.',
        'ru': 'Ставки команды: Общее количество ставок, сделанных вашими нижестоящими за неделю.',
        'fr': 'Paris d\'équipe : Nombre total de paris effectués par vos subordonnés en une semaine.',
        'hi': 'टीम सट्टा: एक सप्ताह में आपके अधीनस्थों द्वारा की गई कुल सट्टेबाज़ी।'
    },
    'invitation_explanation_8': {
        'vi': 'Cấp độ hoa hồng sẽ tính toán lại vào chủ nhật hàng tuần.',
        'en': 'Commission levels are recalculated every Sunday.',
        'ru': 'Уровни комиссии пересчитываются каждое воскресенье.',
        'fr': 'Les niveaux de commission sont recalculés chaque dimanche.',
        'hi': 'कमीशन स्तर प्रत्येक रविवार को पुनः गणना किए जाते हैं।'
    },
    'commission': {
        'vi': 'Hoa hồng',
        'en': 'Commission',
        'ru': 'Комиссия',
        'fr': 'Commission',
        'hi': 'कमीशन'
    },
    'link_copied': {
        'vi': 'Đã sao chép liên kết',
        'en': 'Link copied',
        'ru': 'Ссылка скопирована',
        'fr': 'Lien copié',
        'hi': 'लिंक कॉपी किया गया'
    },
    'referral_code_copied': {
        'vi': 'Đã sao chép mã giới thiệu',
        'en': 'Referral code copied',
        'ru': 'Реферальный код скопирован',
        'fr': 'Code de parrainage copié',
        'hi': 'रेफ़रल कोड कॉपी किया गया'
    },
    'register_referral_code': {
        'vi': 'Đăng ký mã giới thiệu',
        'en': 'Register referral code',
        'ru': 'Регистрация реферального кода',
        'fr': 'Enregistrer le code de parrainage',
        'hi': 'रेफ़रल कोड पंजीकृत करें'
    },
    'confirm_register_referral_code': {
        'vi': 'Xác nhận đăng ký mã giới thiệu {code}',
        'en': 'Confirm registration of referral code {code}',
        'ru': 'Подтвердить регистрацию реферального кода {code}',
        'fr': 'Confirmer l\'enregistrement du code de parrainage {code}',
        'hi': 'रेफ़रल कोड {code} का पंजीकरण पुष्टि करें'
    },
    'register': {
        'vi': 'Đăng ký',
        'en': 'Register',
        'ru': 'Регистрация',
        'fr': 'S\'inscrire',
        'hi': 'पंजीकरण करें'
    },
    'my_investment': {
        'vi': 'Đầu tư của tôi',
        'en': 'My Investment',
        'ru': 'Мои инвестиции',
        'fr': 'Mes investissements',
        'hi': 'मेरे निवेश'
    },
    'guide': {
        'vi': 'HƯỚNG DẪN',
        'en': 'GUIDE',
        'ru': 'ИНСТРУКЦИЯ',
        'fr': 'GUIDE',
        'hi': 'मार्गदर्शिका'
    },
    'add_investment_package': {
        'vi': 'Thêm gói đầu tư',
        'en': 'Add Investment Package',
        'ru': 'Добавить инвестиционный пакет',
        'fr': 'Ajouter un forfait d’investissement',
        'hi': 'निवेश पैकेज जोड़ें'
    },
    'history_30_days': {
        'vi': 'Lịch sử 30 ngày',
        'en': '30-Day History',
        'ru': 'История за 30 дней',
        'fr': 'Historique des 30 jours',
        'hi': '30 दिनों का इतिहास'
    },
    'investment_packages': {
        'vi': 'Các gói đầu tư',
        'en': 'Investment Packages',
        'ru': 'Инвестиционные пакеты',
        'fr': 'Forfaits d’investissement',
        'hi': 'निवेश पैकेज'
    },
    'package': {
        'vi': 'GÓI',
        'en': 'PACKAGE',
        'ru': 'ПАКЕТ',
        'fr': 'FORFAIT',
        'hi': 'पैकेज'
    },
    'investment_amount': {
        'vi': 'MỨC ĐẦU TƯ',
        'en': 'Investment Amount',
        'ru': 'Сумма инвестиций',
        'fr': 'Montant investi',
        'hi': 'निवेश राशि'
    },
    'reward': {
        'vi': 'THƯỞNG',
        'en': 'REWARD',
        'ru': 'НАГРАДА',
        'fr': 'RÉCOMPENSE',
        'hi': 'इनाम'
    },
    'what_is_investment': {
        'vi': 'Đầu tư là gì?',
        'en': 'What is investment?',
        'ru': 'Что такое инвестиции?',
        'fr': 'Qu’est-ce que l’investissement ?',
        'hi': 'निवेश क्या है?'
    },
    'investment_description_1': {
        'vi': 'Đầu tư là 1 hình thức góp vốn nhận lợi nhuận về ví hàng ngày.',
        'en': 'Investment is a form of capital contribution that generates daily profit to your wallet.',
        'ru': 'Инвестиции — это форма вложения капитала, приносящая ежедневную прибыль в ваш кошелёк.',
        'fr': 'L’investissement est une forme de contribution de capital qui génère un profit quotidien vers votre portefeuille.',
        'hi': 'निवेश पूंजी योगदान का एक रूप है जो आपके वॉलेट में दैनिक लाभ उत्पन्न करता है।'
    },
    'investment_description_2': {
        'vi': 'Tiền đầu tư có thể rút khi đến thời gian đáo hạn của gói đầu tư.',
        'en': 'Investment funds can be withdrawn when the investment package reaches its maturity date.',
        'ru': 'Инвестиционные средства можно вывести по окончании срока действия инвестиционного пакета.',
        'fr': 'Les fonds investis peuvent être retirés à l’échéance du forfait d’investissement.',
        'hi': 'निवेश की गई राशि को निवेश पैकेज की परिपक्वता तिथि पर निकाला जा सकता है।'
    },
    'investment_description_3': {
        'vi': 'Các gói đầu tư khác nhau có các lợi ích khác nhau cả về thời gian đáo hạn và mức thưởng lãi hàng ngày.',
        'en': 'Different investment packages offer different benefits in terms of maturity time and daily interest rewards.',
        'ru': 'Разные инвестиционные пакеты предлагают разные преимущества по сроку погашения и ежедневным процентным выплатам.',
        'fr': 'Différents forfaits d’investissement offrent des avantages variés en termes de durée de maturité et de récompenses d’intérêt quotidiennes.',
        'hi': 'विभिन्न निवेश पैकेज परिपक्वता अवधि और दैनिक ब्याज लाभों के मामले में अलग-अलग लाभ प्रदान करते हैं।'
    },
    'investment_description_4': {
        'vi': 'Tiền đầu tư sẽ được phân bổ cho các hoạt động marketing, các giải thưởng ... và lợi nhuận hằng ngày sẽ được phân bổ dựa trên các giao dịch trong ngày.',
        'en': 'Investment funds will be allocated to marketing activities, rewards, etc., and daily profits will be distributed based on daily transactions.',
        'ru': 'Инвестиционные средства будут распределены на маркетинговые активности, призы и т.д., а ежедневная прибыль будет рассчитываться на основе дневных транзакций.',
        'fr': 'Les fonds investis seront répartis entre les activités marketing, les récompenses, etc., et les bénéfices quotidiens seront distribués en fonction des transactions du jour.',
        'hi': 'निवेश राशि का उपयोग मार्केटिंग गतिविधियों, पुरस्कार आदि के लिए किया जाएगा और दैनिक लाभ को दिन की लेन-देन के आधार पर वितरित किया जाएगा।'
    },
    'what_is_maturity_date': {
        'vi': 'Ngày đáo hạn là gì?',
        'en': 'What is the maturity date?',
        'ru': 'Что такое дата погашения?',
        'fr': 'Qu’est-ce que la date d’échéance ?',
        'hi': 'परिपक्वता तिथि क्या है?'
    },
    'maturity_date_description_1': {
        'vi': 'Ngày đáo hạn là thời gian khoá vốn đầu tư. Trong thời gian này, nhà đầu tư không thể rút vốn đầu tư mà chỉ nhận lãi hàng ngày.',
        'en': 'The maturity date is the lock-in period of the investment. During this time, investors cannot withdraw their capital but will receive daily interest.',
        'ru': 'Дата погашения — это период блокировки инвестиционного капитала. В течение этого времени инвесторы не могут вывести средства, но получают ежедневный доход.',
        'fr': 'La date d’échéance correspond à la période de blocage du capital investi. Pendant cette période, les investisseurs ne peuvent pas retirer leur capital, mais reçoivent des intérêts quotidiens.',
        'hi': 'परिपक्वता तिथि निवेश की लॉक-इन अवधि होती है। इस अवधि के दौरान निवेशक अपनी पूंजी नहीं निकाल सकते, लेकिन उन्हें दैनिक ब्याज प्राप्त होता है।'
    },
    'maturity_date_description_2': {
        'vi': 'Các gói đầu tư khác nhau sẽ có ngày đáo hạn khác nhau.',
        'en': 'Different investment packages will have different maturity dates.',
        'ru': 'Разные инвестиционные пакеты имеют разные сроки погашения.',
        'fr': 'Les différents forfaits d’investissement ont des dates d’échéance différentes.',
        'hi': 'विभिन्न निवेश पैकेजों की परिपक्वता तिथियाँ अलग-अलग होती हैं।'
    },
    'maturity_date_description_3': {
        'vi': 'Vốn đầu tư sẽ tự động chuyển về ví khi tới ngày đáo hạn.',
        'en': 'The investment capital will be automatically returned to the wallet on the maturity date.',
        'ru': 'Инвестиционный капитал будет автоматически возвращён в кошелёк по дате погашения.',
        'fr': 'Le capital investi sera automatiquement reversé dans le portefeuille à la date d’échéance.',
        'hi': 'निवेश की गई राशि परिपक्वता तिथि पर स्वचालित रूप से वॉलेट में भेज दी जाएगी।'
    },
    'investment_requirements': {
        'vi': 'Điều kiện tham gia đầu tư?',
        'en': 'Investment participation requirements?',
        'ru': 'Условия участия в инвестициях?',
        'fr': 'Conditions de participation à l’investissement ?',
        'hi': 'निवेश में भाग लेने की शर्तें क्या हैं?'
    },
    'package_capital_requirement': {
        'vi': 'Các gói đầu tư khác nhau có yêu cầu vốn đầu tư khác nhau.',
        'en': 'Different investment packages have different capital requirements.',
        'ru': 'Разные инвестиционные пакеты имеют разные требования к капиталу.',
        'fr': 'Les différents forfaits d’investissement ont des exigences de capital différentes.',
        'hi': 'विभिन्न निवेश पैकेजों की पूंजी आवश्यकताएँ अलग-अलग होती हैं।'
    },
    'what_is_interest_reward': {
        'vi': 'Thưởng lãi là gì?',
        'en': 'What is interest reward?',
        'ru': 'Что такое процентное вознаграждение?',
        'fr': 'Qu’est-ce que la récompense d’intérêt ?',
        'hi': 'ब्याज इनाम क्या है?'
    },
    'interest_reward_description_1': {
        'vi': 'Thưởng lãi là mức lợi nhuận được cộng thêm vào lợi nhuận nhận được hàng ngày của gói đầu tư.',
        'en': 'Interest reward is the additional profit added to the daily return of the investment package.',
        'ru': 'Процентное вознаграждение — это дополнительная прибыль, добавляемая к ежедневному доходу инвестиционного пакета.',
        'fr': 'La récompense d’intérêt est le bénéfice supplémentaire ajouté au rendement quotidien du forfait d’investissement.',
        'hi': 'ब्याज इनाम वह अतिरिक्त लाभ है जो निवेश पैकेज की दैनिक आय में जोड़ा जाता है।'
    },
    'interest_reward_description_2': {
        'vi': 'Mức đầu tư sẽ tồn tại theo gói đầu tư cho đến khi đáo hạn.',
        'en': 'The investment amount will remain in the investment package until maturity.',
        'ru': 'Сумма инвестиций будет оставаться в инвестиционном пакете до даты погашения.',
        'fr': 'Le montant investi restera dans le forfait d’investissement jusqu’à l’échéance.',
        'hi': 'निवेश राशि परिपक्वता तक निवेश पैकेज में बनी रहेगी।'
    },
    'open_investment_package': {
        'vi': 'MỞ GÓI ĐẦU TƯ',
        'en': 'OPEN INVESTMENT PACKAGE',
        'ru': 'ОТКРЫТЬ ИНВЕСТИЦИОННЫЙ ПАКЕТ',
        'fr': 'OUVRIR UN FORFAIT D’INVESTISSEMENT',
        'hi': 'निवेश पैकेज खोलें'
    },
    'select_investment_package': {
        'vi': 'CHỌN GÓI ĐẦU TƯ',
        'en': 'SELECT INVESTMENT PACKAGE',
        'ru': 'ВЫБЕРИТЕ ИНВЕСТИЦИОННЫЙ ПАКЕТ',
        'fr': 'SÉLECTIONNER UN FORFAIT D’INVESTISSEMENT',
        'hi': 'निवेश पैकेज चुनें'
    },
    'requirement': {
        'vi': 'Yêu cầu',
        'en': 'Requirement',
        'ru': 'Требование',
        'fr': 'Exigence',
        'hi': 'आवश्यकता'
    },
    'interest_reward': {
        'vi': 'Thưởng lãi',
        'en': 'Interest Reward',
        'ru': 'Процентная премия',
        'fr': 'Récompense d’intérêt',
        'hi': 'ब्याज इनाम'
    },
    'maturity': {
        'vi': 'Đáo hạn',
        'en': 'Maturity',
        'ru': 'Срок погашения',
        'fr': 'Échéance',
        'hi': 'परिपक्वता'
    },
    'investment_capital': {
        'vi': 'Vốn đầu tư:',
        'en': 'Investment Capital:',
        'ru': 'Инвестиционный капитал:',
        'fr': 'Capital d’investissement :',
        'hi': 'निवेश पूंजी:'
    },
    'go_back': {
        'vi': 'Quay lại',
        'en': 'Back',
        'ru': 'Назад',
        'fr': 'Retour',
        'hi': 'वापस जाएं'
    },
    'next': {
        'vi': 'Tiếp theo',
        'en': 'Next',
        'ru': 'Далее',
        'fr': 'Suivant',
        'hi': 'अगला'
    },
    'package_history': {
        'vi': 'Lịch sử gói',
        'en': 'Package History',
        'ru': 'История пакета',
        'fr': 'Historique du forfait',
        'hi': 'पैकेज इतिहास'
    },
    'interest': {
        'vi': 'Lãi',
        'en': 'Interest',
        'ru': 'Проценты',
        'fr': 'Intérêt',
        'hi': 'ब्याज'
    },
    'start_date': {
        'vi': 'Ngày bắt đầu',
        'en': 'Start Date',
        'ru': 'Дата начала',
        'fr': 'Date de début',
        'hi': 'प्रारंभ तिथि'
    },
    'profit': {
        'vi': 'Lợi nhuận',
        'en': 'Profit',
        'ru': 'Прибыль',
        'fr': 'Profit',
        'hi': 'लाभ'
    },
    'no_data': {
        'vi': 'Chưa có dữ liệu',
        'en': 'No data available',
        'ru': 'Нет данных',
        'fr': 'Aucune donnée disponible',
        'hi': 'कोई डेटा उपलब्ध नहीं है'
    },
    'name': {
        'vi': 'Tên',
        'en': 'Name',
        'ru': 'Имя',
        'fr': 'Nom',
        'hi': 'नाम'
    },
    'balance': {
        'vi': 'Số dư',
        'en': 'Balance',
        'ru': 'Баланс',
        'fr': 'Solde',
        'hi': 'शेष राशि'
    },
    'promotion': {
        'vi': 'Khuyến mãi',
        'en': 'Promotion',
        'ru': 'Акция',
        'fr': 'Promotion',
        'hi': 'प्रमोशन'
    },
    'internal': {
        'vi': 'Nội bộ',
        'en': 'Internal',
        'ru': 'Внутренний',
        'fr': 'Interne',
        'hi': 'आंतरिक'
    },
    'deposit_withdraw': {
        'vi': 'Nạp Rút',
        'en': 'Deposit & Withdraw',
        'ru': 'Пополнение и Вывод',
        'fr': 'Dépôt & Retrait',
        'hi': 'जमा और निकासी'
    },
    'participating': {
        'vi': 'Đang tham gia',
        'en': 'Participating',
        'ru': 'Участвует',
        'fr': 'Participe',
        'hi': 'भाग ले रहा है'
    },
    'promotion_package': {
        'vi': 'Gói khuyến mãi',
        'en': 'Promotion Package',
        'ru': 'Промо-пакет',
        'fr': 'Forfait promotionnel',
        'hi': 'प्रमोशन पैकेज'
    },
    'promo_package_note_1': {
        'vi': 'Gói khuyến mãi sẽ xuất hiện 1 lần hoặc theo sự kiện',
        'en': 'The promotion package will appear once or during events',
        'ru': 'Промо-пакет появляется один раз или во время событий',
        'fr': 'Le forfait promotionnel apparaît une fois ou lors d\'événements',
        'hi': 'प्रमोशन पैकेज एक बार या किसी इवेंट के दौरान दिखाई देगा'
    },
    'promo_package_note_2': {
        'vi': 'Tiền khuyến mãi sẽ cộng ngay lập tức vào gói khuyến mãi khi đăng ký.',
        'en': 'Promotional funds will be added immediately to the promotion package upon registration.',
        'ru': 'Промо-средства будут немедленно добавлены к промо-пакету при регистрации.',
        'fr': 'Les fonds promotionnels seront ajoutés immédiatement au forfait promotionnel lors de l\'inscription.',
        'hi': 'प्रमोशनल राशि रजिस्ट्रेशन करते ही तुरंत प्रोमोशन पैकेज में जोड़ दी जाएगी।'
    },
    'promo_package_note_3': {
        'vi': 'Sau khi hoàn thành các mục tiêu, bạn có thể rút vốn, tiền khuyến mãi, và tất cả lợi nhuận về tài khoản chính.',
        'en': 'After completing the goals, you can withdraw your capital, promotional funds, and all profits to your main account.',
        'ru': 'После выполнения целей вы можете вывести капитал, промо-средства и всю прибыль на основной счет.',
        'fr': 'Une fois les objectifs atteints, vous pouvez retirer votre capital, les fonds promotionnels et tous les bénéfices vers votre compte principal.',
        'hi': 'लक्ष्यों को पूरा करने के बाद, आप अपनी पूंजी, प्रमोशनल राशि और सभी लाभ अपने मुख्य खाते में निकाल सकते हैं।'
    },
    'promo_package_note_4': {
        'vi': 'Trong trò chơi, bạn chọn số tiền loại ví để đặt cược ở góc trên bên phải, chọn ví khuyến mãi.',
        'en': 'In the game, select the wallet type and amount to bet at the top right corner, choose the promotion wallet.',
        'ru': 'В игре выберите тип кошелька и сумму ставки в правом верхнем углу, выберите промо-кошелёк.',
        'fr': 'Dans le jeu, sélectionnez le type de portefeuille et le montant à miser en haut à droite, choisissez le portefeuille promotionnel.',
        'hi': 'खेल में, दाएं ऊपर कोने में वॉलेट का प्रकार और राशि चुनें और प्रमोशनल वॉलेट को चुनें।'
    },
    'promo_package_note_5': {
        'vi': 'Nếu không hoàn thành mục tiêu trong thời gian khuyến mãi, hoặc không hoàn thành mục tiêu mà kết thúc sớm gói khuyến mãi, bạn sẽ nhận được 100% vốn và 60% lợi nhuận nếu kết quả lợi nhuận đang dương. Hoặc Vốn - Lợi nhuận nếu lợi nhuận đang âm.',
        'en': 'If you do not complete the goal during the promotion period or end the promotion package early without completing it, you will receive 100% of your capital and 60% of the profit if the result is positive. Or Capital minus Loss if the result is negative.',
        'ru': 'Если цель не достигнута в период действия промоакции или промо-пакет завершён досрочно без выполнения цели, вы получите 100% капитала и 60% прибыли, если результат положительный. Или капитал минус убыток, если результат отрицательный.',
        'fr': 'Si vous ne terminez pas l’objectif pendant la période promotionnelle ou terminez le forfait promotionnel plus tôt sans l’atteindre, vous recevrez 100 % du capital et 60 % du profit si le résultat est positif. Sinon, le capital moins la perte si le résultat est négatif.',
        'hi': 'यदि आप प्रोमोशन अवधि में लक्ष्य पूरा नहीं करते हैं या प्रोमो पैकेज को अधूरा छोड़कर जल्दी समाप्त करते हैं, तो आपको 100% पूंजी और 60% लाभ मिलेगा यदि लाभ सकारात्मक है। या पूंजी में से नुकसान घटाया जाएगा यदि लाभ नकारात्मक है।'
    },
    'promo_package_note_6': {
        'vi': 'Bạn có thể dừng gói khuyến mãi bất cứ lúc nào, dù chưa thực hiện giao dịch nào.',
        'en': 'You can stop the promotion package at any time, even if no transaction has been made.',
        'ru': 'Вы можете остановить промо-пакет в любое время, даже если не было совершено ни одной сделки.',
        'fr': 'Vous pouvez arrêter le forfait promotionnel à tout moment, même si aucune transaction n’a été effectuée.',
        'hi': 'आप प्रमोशन पैकेज को कभी भी रोक सकते हैं, भले ही कोई लेन-देन न किया गया हो।'
    },
    'internal_transfer': {
        'vi': 'CHUYỂN TIỀN NỘI BỘ',
        'en': 'INTERNAL TRANSFER',
        'ru': 'ВНУТРЕННИЙ ПЕРЕВОД',
        'fr': 'TRANSFERT INTERNE',
        'hi': 'आंतरिक ट्रांसफर'
    },
    'receiver_uid': {
        'vi': 'UID nhận:',
        'en': 'Receiver UID:',
        'ru': 'UID получателя:',
        'fr': 'UID du destinataire :',
        'hi': 'प्राप्तकर्ता UID:'
    },
    'transfer_amount': {
        'vi': 'Số tiền chuyển',
        'en': 'Transfer Amount',
        'ru': 'Сумма перевода',
        'fr': 'Montant du transfert',
        'hi': 'ट्रांसफर राशि'
    },
    'confirm': {
        'vi': 'Xác nhận',
        'en': 'Confirm',
        'ru': 'Подтвердить',
        'fr': 'Confirmer',
        'hi': 'पुष्टि करें'
    },
    'crypto_wallet': {
        'vi': 'Ví tiền điện tử',
        'en': 'Crypto Wallet',
        'ru': 'Криптовалютный кошелёк',
        'fr': 'Portefeuille crypto',
        'hi': 'क्रिप्टो वॉलेट'
    },
    'deposit': {
        'vi': 'Nạp',
        'en': 'Deposit',
        'ru': 'Пополнение',
        'fr': 'Dépôt',
        'hi': 'जमा'
    },
    'withdraw': {
        'vi': 'Rút',
        'en': 'Withdraw',
        'ru': 'Вывод',
        'fr': 'Retrait',
        'hi': 'निकासी'
    },
    'content': {
        'vi': 'Nội dung',
        'en': 'Content',
        'ru': 'Содержание',
        'fr': 'Contenu',
        'hi': 'सामग्री'
    },
    'amount': {
        'vi': 'Số tiền',
        'en': 'Amount',
        'ru': 'Сумма',
        'fr': 'Montant',
        'hi': 'राशि'
    },
    'enter_usdt_wallet': {
        'vi': 'Nhập ví rút USDT BEP20',
        'en': 'Enter USDT BEP20 withdrawal wallet',
        'ru': 'Введите адрес кошелька для вывода USDT BEP20',
        'fr': 'Entrez le portefeuille de retrait USDT BEP20',
        'hi': 'USDT BEP20 निकासी वॉलेट दर्ज करें'
    },
    'withdraw_amount': {
        'vi': 'Số tiền rút',
        'en': 'Withdrawal Amount',
        'ru': 'Сумма вывода',
        'fr': 'Montant du retrait',
        'hi': 'निकासी राशि'
    },
    'register_promo': {
        'vi': 'ĐĂNG KÝ KHUYẾN MÃI',
        'en': 'REGISTER PROMOTION',
        'ru': 'РЕГИСТРАЦИЯ АКЦИИ',
        'fr': 'S’INSCRIRE À LA PROMOTION',
        'hi': 'प्रमोशन के लिए पंजीकरण करें'
    },
    'participation_fund': {
        'vi': 'Vốn tham gia',
        'en': 'Participation Fund',
        'ru': 'Участный капитал',
        'fr': 'Fonds de participation',
        'hi': 'भागीदारी पूंजी'
    },
    'cancel': {
        'vi': 'Huỷ',
        'en': 'Cancel',
        'ru': 'Отмена',
        'fr': 'Annuler',
        'hi': 'रद्द करें'
    },
    'transfer_confirm': {
        'vi': 'Xác nhận chuyển',
        'en': 'Transfer Confirm',
        'ru': 'Подтверждение перевода',
        'fr': 'Confirmation du transfert',
        'hi': 'स्थानांतरण की पुष्टि करें'
    },
    'confirm_transfer_text': {
        'vi': 'Xác nhận chuyển $ {amount} đến UID {uid} - {name}',
        'en': 'Confirm transfer of $ {amount} to UID {uid} - {name}',
        'ru': 'Подтвердите перевод $ {amount} на UID {uid} - {name}',
        'fr': 'Confirmer le transfert de $ {amount} vers l’UID {uid} - {name}',
        'hi': 'UID {uid} - {name} को $ {amount} ट्रांसफर की पुष्टि करें'
    },
    'from_uid': {
        'vi': 'Nhận từ {uid}',
        'en': 'Received from {uid}',
        'ru': 'Получено от {uid}',
        'fr': 'Reçu de {uid}',
        'hi': '{uid} से प्राप्त किया गया'
    },
    'sent_to_uid': {
        'vi': 'Gửi đến {uid}',
        'en': 'Sent to {uid}',
        'ru': 'Отправлено на {uid}',
        'fr': 'Envoyé à {uid}',
        'hi': '{uid} को भेजा गया'
    },
    'completed': {
        'vi': 'Hoàn thành',
        'en': 'Completed',
        'ru': 'Завершено',
        'fr': 'Terminé',
        'hi': 'पूर्ण हुआ'
    },
    'queue': {
        'vi': 'Hàng chờ',
        'en': 'Queue',
        'ru': 'Очередь',
        'fr': 'File d’attente',
        'hi': 'प्रतीक्षा सूची'
    },
    'reject': {
        'vi': 'Từ chối',
        'en': 'Reject',
        'ru': 'Отклонить',
        'fr': 'Refuser',
        'hi': 'अस्वीकार करें'
    },
    'cancel_promotion': {
        'vi': 'Huỷ khuyến mãi {name}',
        'en': 'Cancel promotion {name}',
        'ru': 'Отменить акцию {name}',
        'fr': 'Annuler la promotion {name}',
        'hi': 'प्रमोशन {name} रद्द करें'
    },
    'wallet_not_ready': {
        'vi': 'Ví chưa sẵn sàng',
        'en': 'Wallet not ready',
        'ru': 'Кошелёк не готов',
        'fr': 'Portefeuille non prêt',
        'hi': 'वॉलेट तैयार नहीं है'
    },
    'time_remaining': {
        'vi': 'Thời gian còn lại',
        'en': 'Time remaining',
        'ru': 'Оставшееся время',
        'fr': 'Temps restant',
        'hi': 'शेष समय'
    },
    'wingo_1m': {
        'vi': 'Win Go 1 phút',
        'en': 'Win Go 1 Minute',
        'ru': 'Win Go 1 минута',
        'fr': 'Win Go 1 minute',
        'hi': 'Win Go 1 मिनट'
    },
    'green': {
        'vi': 'Xanh',
        'en': 'Green',
        'ru': 'Зелёный',
        'fr': 'Vert',
        'hi': 'हरा'
    },
    'purple': {
        'vi': 'Tím',
        'en': 'Purple',
        'ru': 'Фиолетовый',
        'fr': 'Violet',
        'hi': 'बैंगनी'
    },
    'red': {
        'vi': 'Đỏ',
        'en': 'Red',
        'ru': 'Красный',
        'fr': 'Rouge',
        'hi': 'लाल'
    },
    'big': {
        'vi': 'Lớn',
        'en': 'Big',
        'ru': 'Большое',
        'fr': 'Grand',
        'hi': 'बड़ा'
    },
    'small': {
        'vi': 'Nhỏ',
        'en': 'Small',
        'ru': 'Маленькое',
        'fr': 'Petit',
        'hi': 'छोटा'
    },
    'my_history': {
        'vi': 'LỊCH SỬ CỦA TÔI',
        'en': 'MY HISTORY',
        'ru': 'МОЯ ИСТОРИЯ',
        'fr': 'MON HISTORIQUE',
        'hi': 'मेरा इतिहास'
    },
    'number': {
        'vi': 'Số',
        'en': 'Number',
        'ru': 'Число',
        'fr': 'Nombre',
        'hi': 'संख्या'
    },
    'big_small': {
        'vi': 'Lớn nhỏ',
        'en': 'Big Small',
        'ru': 'Больше Меньше',
        'fr': 'Grand Petit',
        'hi': 'बड़ा छोटा'
    },
    'color': {
        'vi': 'Màu sắc',
        'en': 'Color',
        'ru': 'Цвет',
        'fr': 'Couleur',
        'hi': 'रंग'
    },
    'statistics': {
        'vi': 'Thống kê',
        'en': 'Statistics',
        'ru': 'Статистика',
        'fr': 'Statistiques',
        'hi': 'आँकड़े'
    },
    'draw_round': {
        'vi': 'Kỳ xổ',
        'en': 'Draw Round',
        'ru': 'Тираж',
        'fr': 'Tirage',
        'hi': 'ड्रा दौर'
    },
    'placing': {
        'vi': 'Đang đặt',
        'en': 'Placing',
        'ru': 'Ставка',
        'fr': 'En cours de mise',
        'hi': 'लगाया जा रहा है'
    },
    'send': {
        'vi': 'GỬI',
        'en': 'SEND',
        'ru': 'ОТПРАВИТЬ',
        'fr': 'ENVOYER',
        'hi': 'भेजें'
    },
    'bet_wingo': {
        'vi': 'Đặt cược WIN GO',
        'en': 'Place Bet on WIN GO',
        'ru': 'Сделать ставку на WIN GO',
        'fr': 'Parier sur WIN GO',
        'hi': 'WIN GO पर दांव लगाएं'
    },
    'select': {
        'vi': 'Chọn',
        'en': 'Select',
        'ru': 'Выбрать',
        'fr': 'Choisir',
        'hi': 'चुनें'
    },
    'place_success': {
        'vi': 'Đặt thành công',
        'en': 'Placed Successfully',
        'ru': 'Успешно размещено',
        'fr': 'Placement réussi',
        'hi': 'सफलतापूर्वक लगाया गया'
    },
    'bet_amount': {
        'vi': 'Số tiền cược',
        'en': 'Bet Amount',
        'ru': 'Сумма ставки',
        'fr': 'Montant du pari',
        'hi': 'शर्त की राशि'
    },
    'commission_level': {
        'vi': 'Cấp độ hoa hồng',
        'en': 'Commission Level',
        'ru': 'Уровень комиссии',
        'fr': 'Niveau de commission',
        'hi': 'कमीशन स्तर'
    },
    'commission_percent': {
        'vi': 'Phần trăm hoa hồng',
        'en': 'Commission Percentage',
        'ru': 'Процент комиссии',
        'fr': 'Pourcentage de commission',
        'hi': 'कमीशन प्रतिशत'
    },
    'commission_received': {
        'vi': 'Hoa hồng nhận',
        'en': 'Commission Received',
        'ru': 'Полученная комиссия',
        'fr': 'Commission reçue',
        'hi': 'प्राप्त कमीशन'
    },
    'bet_type': {
        'vi': 'Loại hình cược',
        'en': 'Bet Type',
        'ru': 'Тип ставки',
        'fr': 'Type de pari',
        'hi': 'शर्त का प्रकार'
    },
    'no_promotion': {
        'vi': 'Chưa có chương trình khuyến mãi',
        'en': 'No promotion available',
        'ru': 'Нет доступных акций',
        'fr': 'Aucune promotion disponible',
        'hi': 'कोई प्रचार उपलब्ध नहीं है'
    },
    'unique': {
        'vi': 'Duy nhất',
        'en': 'Unique',
        'ru': 'Уникальный',
        'fr': 'Unique',
        'hi': 'अद्वितीय'
    },
    'event': {
        'vi': 'Sự kiện',
        'en': 'Event',
        'ru': 'Событие',
        'fr': 'Événement',
        'hi': 'घटना'
    },
    'under': {
        'vi': 'Dưới',
        'en': 'Under',
        'ru': 'Ниже',
        'fr': 'Sous',
        'hi': 'नीचे'
    },
    'any_capital': {
        'vi': 'Vốn bất kỳ',
        'en': 'Any capital',
        'ru': 'Любой капитал',
        'fr': 'N’importe quel capital',
        'hi': 'कोई भी पूंजी'
    },
    'greater_than_amount': {
        'vi': 'Lớn hơn $ {amount}',
        'en': 'Greater than $ {amount}',
        'ru': 'Больше $ {amount}',
        'fr': 'Supérieur à $ {amount}',
        'hi': '$ {amount} से अधिक'
    },
    'from_to_amount': {
        'vi': 'Từ $ {amount_from} đến $ {amount_to}',
        'en': 'From $ {amount_from} to $ {amount_to}',
        'ru': 'От $ {amount_from} до $ {amount_to}',
        'fr': 'De $ {amount_from} à $ {amount_to}',
        'hi': '$ {amount_from} से $ {amount_to} तक'
    },
    'complete_bets': {
        'vi': 'Hoàn thành {required_order} lần đặt cược',
        'en': 'Complete {required_order} bets',
        'ru': 'Сделайте {required_order} ставок',
        'fr': 'Effectuez {required_order} mises',
        'hi': '{required_order} बार सट्टा पूरा करें'
    },
    'win_percent_capital': {
        'vi': 'Chiến thắng {required_profit}% vốn',
        'en': 'Win {required_profit}% of capital',
        'ru': 'Выиграйте {required_profit}% капитала',
        'fr': 'Gagnez {required_profit}% du capital',
        'hi': '{required_profit}% पूंजी जीतें'
    },
    'no_requirement': {
        'vi': 'Không có yêu cầu',
        'en': 'No requirement',
        'ru': 'Нет требований',
        'fr': 'Aucune exigence',
        'hi': 'कोई आवश्यकता नहीं'
    },
    'no_deadline': {
        'vi': 'Không có thời hạn',
        'en': 'No deadline',
        'ru': 'Без срока',
        'fr': 'Aucune échéance',
        'hi': 'कोई समय सीमा नहीं'
    },
    'category': {
        'vi': 'Thể loại',
        'en': 'Category',
        'ru': 'Категория',
        'fr': 'Catégorie',
        'hi': 'श्रेणी'
    },
    'apply': {
        'vi': 'Áp dụng',
        'en': 'Apply',
        'ru': 'Применить',
        'fr': 'Appliquer',
        'hi': 'लागू करें'
    },
    'capital': {
        'vi': 'Vốn',
        'en': 'Capital',
        'ru': 'Капитал',
        'fr': 'Capital',
        'hi': 'पूंजी'
    },
    'order_target': {
        'vi': 'Mục tiêu lệnh',
        'en': 'Order target',
        'ru': 'Цель ордера',
        'fr': 'Objectif de l’ordre',
        'hi': 'ऑर्डर लक्ष्य'
    },
    'profit_target': {
        'vi': 'Mục tiêu lợi nhuận',
        'en': 'Profit target',
        'ru': 'Целевая прибыль',
        'fr': 'Objectif de profit',
        'hi': 'लाभ लक्ष्य'
    },
    'deadline': {
        'vi': 'Thời hạn',
        'en': 'Deadline',
        'ru': 'Срок',
        'fr': 'Échéance',
        'hi': 'समय सीमा'
    },
    'not_joined_promotion': {
        'vi': 'Chưa tham gia chương trình khuyến mãi',
        'en': 'Not joined the promotion program',
        'ru': 'Не участвовал в акции',
        'fr': "N'a pas rejoint le programme de promotion",
        'hi': 'प्रमोशन कार्यक्रम में शामिल नहीं हुए हैं'
    },
    'order': {
        'vi': 'Lệnh',
        'en': 'Order',
        'ru': 'Ордер',
        'fr': 'Ordre',
        'hi': 'ऑर्डर'
    },
    'less_than_amount': {
        'vi': 'Nhỏ hơn $ {amount}',
        'en': 'Less than $ {amount}',
        'ru': 'Меньше $ {amount}',
        'fr': 'Moins de $ {amount}',
        'hi': '${amount} से कम'
    },
    'lose': {
        'vi': 'Thua',
        'en': 'Lose',
        'ru': 'Проиграл',
        'fr': 'Perdu',
        'hi': 'हारा'
    },
    'win': {
        'vi': 'Thắng',
        'en': 'Win',
        'ru': 'Победа',
        'fr': 'Gagné',
        'hi': 'जीता'
    },
    'purchase_amount': {
        'vi': 'Số tiền mua',
        'en': 'Purchase Amount',
        'ru': 'Сумма покупки',
        'fr': 'Montant de l\'achat',
        'hi': 'खरीद राशि'
    },
    'tax': {
        'vi': 'Thuế',
        'en': 'Tax',
        'ru': 'Налог',
        'fr': 'Taxe',
        'hi': 'कर'
    },
    'after_tax_amount': {
        'vi': 'Tiền sau thuế',
        'en': 'Amount After Tax',
        'ru': 'Сумма после налога',
        'fr': 'Montant après impôt',
        'hi': 'कर के बाद राशि'
    },
    'result': {
        'vi': 'Kết quả',
        'en': 'Result',
        'ru': 'Результат',
        'fr': 'Résultat',
        'hi': 'परिणाम'
    },
    'status': {
        'vi': 'Tình trạng',
        'en': 'Status',
        'ru': 'Статус',
        'fr': 'Statut',
        'hi': 'स्थिति'
    },
    'win_lose': {
        'vi': 'Thắng thua',
        'en': 'Win or Lose',
        'ru': 'Выигрыш или проигрыш',
        'fr': 'Gagné ou perdu',
        'hi': 'जीत या हार'
    },
    'created_time': {
        'vi': 'Thời gian tạo',
        'en': 'Created Time',
        'ru': 'Время создания',
        'fr': 'Heure de création',
        'hi': 'बनाने का समय'
    },
    'investment_channel': {
        'vi': 'KÊNH ĐẦU TƯ',
        'en': 'INVESTMENT CHANNEL',
        'ru': 'ИНВЕСТИЦИОННЫЙ КАНАЛ',
        'fr': 'CANAL D\'INVESTISSEMENT',
        'hi': 'निवेश चैनल'
    },
    'connection': {
        'vi': 'Kết nối',
        'en': 'Connection',
        'ru': 'Подключение',
        'fr': 'Connexion',
        'hi': 'कनेक्शन'
    },
    'restore': {
        'vi': 'Khôi phục',
        'en': 'Restore',
        'ru': 'Восстановить',
        'fr': 'Restaurer',
        'hi': 'पुनर्स्थापित करें'
    }
}