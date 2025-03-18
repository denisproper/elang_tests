from faker import Faker

fake = Faker()

valid_data = [
    (fake.first_name(), fake.email(), fake.sentence()),
    (fake.first_name(), fake.email(), "Программирование — это искусство создания кода, которое решает задачи и автоматизирует процессы. Разработка включает анализ, проектирование, кодирование, тестирование и поддержку. Важно писать чистый и понятный код, следовать принципам SOLID, DRY и KISS. Использование Git помогает контролировать версии, а автоматизированное тестирование гарантирует надёжность. Языки программирования, такие как Python, JavaScript и Java, позволяют реализовать проекты разного уровня. Разработка веб-приложений, мобильных приложений и систем машинного обучения требует знания фреймворков и библиотек. Docker и Kubernetes обеспечивают удобное развертывание сервисов. Современные технологии, такие как облачные вычисления и микросервисы, упрощают масштабирование. Разработчики постоянно учатся, осваивают новые технологии и инструменты. Главное — логика, практика и стремление к совершенствованиюkwjerjwerkjweljrkwejrlkwjelrjwelkrjlkwejlrlwekwerjklwjerkjwelkrjlwejrlkwejlrwerwe,mr,nwemrnw,enr,wne,rwemnrm,wenr,mnew,rn"),
    (fake.first_name(), fake.email(), fake.paragraph(nb_sentences=5)),
    (fake.first_name()[:2], fake.email(), fake.sentence()),
    (fake.first_name()[:13], fake.email(), fake.sentence()),
    (fake.user_name(), fake.email(), fake.sentence())
]
