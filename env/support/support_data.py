from faker import Faker

fake = Faker()

class SupportData:

    @staticmethod
    def get_valid_data():
        return [
            (fake.first_name()[:13], fake.email(), fake.sentence()),
            (fake.first_name()[:13], fake.email(), "Программирование — это искусство создания кода, которое решает задачи и автоматизирует процессы. Разработка включает анализ, проектирование, кодирование, тестирование и поддержку. Важно писать чистый и понятный код, следовать принципам SOLID, DRY и KISS. Использование Git помогает контролировать версии, а автоматизированное тестирование гарантирует надёжность. Языки программирования, такие как Python, JavaScript и Java, позволяют реализовать проекты разного уровня. Разработка веб-приложений, мобильных приложений и систем машинного обучения требует знания фреймворков и библиотек. Docker и Kubernetes обеспечивают удобное развертывание сервисов. Современные технологии, такие как облачные вычисления и микросервисы, упрощают масштабирование. Разработчики постоянно учатся, осваивают новые технологии и инструменты. Главное — логика, практика и стремление к совершенствованиюkwjerjwerkjweljrkwejrlkwjelrjwelkrjlkwejlrlwekwerjklwjerkjwelkrjlwejrlkwejlrwerwe,mr,nwemrnw,enr,wne,rwemnrm,wenr,mnew,rn"),
            (fake.first_name()[:13], fake.email(), fake.paragraph(nb_sentences=5)),
            (fake.first_name()[:2], fake.email(), fake.sentence()),
            (fake.first_name()[:13], fake.email(), fake.sentence()),
            (fake.user_name()[:13], fake.email(), fake.sentence())
        ]

    @staticmethod
    def get_invalid_name_data():
        return [
            ((fake.first_name() + "x" * 13)[:14], fake.email(), fake.sentence()),
            (fake.first_name()[0], fake.email(), fake.sentence()),
        ]


    @staticmethod
    def get_invalid_email_data():
        return [
            (fake.first_name(), fake.user_name() + "example.com", fake.sentence()),
            (fake.first_name(), fake.email().replace('@', '@@'), fake.sentence()),
            (fake.first_name(), fake.user_name() + "@", fake.sentence()),
            (fake.first_name(), fake.first_name() + " " + fake.email(), fake.sentence()),
            (fake.first_name(), "@example.com", fake.sentence()),
            (fake.first_name(), "abc123!@#$%", fake.sentence()),
        ]

    @staticmethod
    def get_invalid_message_data():
        long_text = fake.text(max_nb_chars=900)
        long_message = long_text + "x" * (1001 - len(long_text))

        return [
            (fake.first_name(), fake.email(), "Test"),
            (fake.first_name(), fake.email(), long_message),
        ]

    @staticmethod
    def get_empty_message_data():
        return [
            (fake.first_name(), fake.email(), "")
        ]
