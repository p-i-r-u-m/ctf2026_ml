<script setup lang="ts">
import { onMounted, ref } from 'vue'
import logo from "../assets/logo.svg";
import Footer from "../components/Footer.vue";
import Button from '../components/Button.vue'


onMounted(() => {
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('reveal-visible');
            }
        });
    }, { threshold: 0.1 });

    const targets = document.querySelectorAll('.reveal');
    targets.forEach(t => observer.observe(t));
});
</script>
<template>
    <div class="mx-auto min-h-screen flex flex-col py-32pt px-32pt md:py-32pt md:px-64pt">
        <header class="flex justify-between items-end pb-128pt">
            <RouterLink to="/" class="transition-opacity hover:opacity-70 active:scale-95">
                <img :src="logo" alt="Logo" class="h-8 md:h-10 w-auto" />
            </RouterLink>
            <p>IT Responsible</p>
        </header>

        <main class="grow flex flex-col">
            <h2 class="font-mono">I wanna be</h2>
            <h1 class="font-mono text-ui-accent pb-96pt uppercase tracking-tighter">IT Responsible</h1>

            <section class="w-full md:w-1/2 pb-64pt reveal">
                <h2 class="font-mono pb-16pt border-b border-ui-white/10">Хто я?</h2>
                <p class="pt-16pt">
                    Привіт! Уявімо, що ти мене ніколи не бачив. Хто ж я такий? Яким чином мене можна описати? Та що
                    вказує на мою
                    готовність та мотивацію стати членом кортіми CTF.
                </p>
            </section>

            <section class="w-full md:w-1/2 md:self-end pb-64pt reveal">
                <h2 class="font-mono pb-16pt border-b border-ui-white/10">Чому саме CTF?</h2>
                <p class="pt-16pt">
                    Цікаве питання, на яке, мабуть, дуже дивно відповідати щось типу “тому що я обожнюю та люблю його”.
                    Я не знаю.
                    Поки що. Я сподіваюсь, що я полюблю CTF усім серцем і це буде неймовірний досвід, проте наразі я
                    можу пояснити
                    це лише прагматично.
                    У BEST великий вибір подач у кортіми. Але не всі із них – технічні, та дозволяють створити щось в
                    айтішній
                    сфері, яка мені подобається. CTF дозволяє мені отримати досвід налагодження технічної інфраструктури
                    івенту,
                    щоб цим користувалось потім декілька десятків людей.
                </p>
            </section>

            <section class="w-full md:w-1/2 pb-64pt reveal">
                <h2 class="font-mono pb-16pt border-b border-ui-white/10">Контент чи айтішник?</h2>
                <p class="pt-16pt">
                    Все таки, я хочу бути контентом. Проте, якщо за якоїсь причини ти не можеш мене ним взяти, я готовий
                    і хотів би отримати досвід IT Responsible. Я все одно хочу попасти в кортіму CTF у такому випадку.
                    Заради отримання Бестівського досвіду у новій кортімі та прокачки моїх hard- та soft-
                    скілів.
                </p>
            </section>

            <section class="w-full md:w-1/2 md:self-end pb-96pt reveal">
                <h2 class="font-mono pb-16pt border-b border-ui-white/10">Мій бекграунд</h2>
                <p class="pt-16pt pb-32pt">
                    У організації CTF-змагань ні. У проходженні – так. Я цікавився деякий час кібербезпекою і навіть
                    думав
                    поступити на цю спеціальність. За цей час я встиг спробувати поклацати такі платформи, як
                    HackTheBox, picoCTF,
                    та навіть брав участь в одних CTF-змаганнях, організованих Маріупольським університетом, які були у
                    форматі
                    Jeopardy.
                </p>

                <section class="reveal">


                    <a href="https://drive.google.com/file/d/1COYt0R7lptTXdkpRDaf2y8FMN7b3lXGM/view?usp=sharing"
                        target="_blank"
                        class="group block w-full border-[3px] border-ui-white/20 hover:border-ui-accent bg-ui-white/5 hover:bg-ui-accent/5 transition-all duration-300 p-16pt relative overflow-hidden">

                        <div
                            class="absolute top-0 right-0 p-4pt font-mono text-[10px] opacity-20 group-hover:opacity-100 group-hover:text-ui-accent transition-opacity">

                            [PDF]

                        </div>


                        <div class="flex items-center gap-24pt">

                            <div
                                class="w-64pt h-64pt bg-ui-white/10 flex items-center justify-center shrink-0 border border-ui-white/10 group-hover:border-ui-accent/30 transition-colors">

                                <svg class="w-32pt h-32pt opacity-40 group-hover:opacity-100 group-hover:text-ui-accent transition-all"
                                    fill="none" stroke="currentColor" viewBox="0 0 24 24">

                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"
                                        d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />

                                </svg>

                            </div>


                            <div class="font-mono">

                                <h3
                                    class="text-sm md:text-base mb-4pt uppercase tracking-wider group-hover:text-ui-accent transition-colors">

                                    CTF_.pdf

                                </h3>

                                <div class="text-[10px] opacity-50 flex flex-col gap-2pt">

                                    <span>SIZE: 521 KB</span>

                                    <span>FORMAT: PDF</span>

                                    <span
                                        class="text-ui-accent opacity-0 group-hover:opacity-100 transition-opacity">>>>
                                        CLICK TO

                                        OPEN</span>

                                </div>

                            </div>

                        </div>

                    </a>

                </section>
            </section>


            <section class="w-full md:w-1/2 md:self-end pb-64pt reveal">
                <h2 class="font-mono pb-16pt border-b border-ui-white/10">Мої плани на 6 місяців</h2>
                <p class="pt-16pt">
                    Я планую залишатися у Львові: навчання в університеті, робота, можливо — пошук нових викликів. Мій
                    графік
                    стабільний, тому я буду відкритий та доступний для кортіми більшу частину часу протягом усього
                    періоду
                    підготовки.
                </p>
            </section>

            <section class="w-full md:w-1/2 pb-64pt reveal">
                <h2 class="font-mono pb-16pt border-b border-ui-white/10">Пріоритет кортіми</h2>
                <div class="pt-16pt font-mono text-sm md:text-base">
                    <ul class="flex flex-col gap-8pt">
                        <li class="opacity-40">01. Здоров'я</li>
                        <li class="opacity-40">02. Робота, університет</li>
                        <li class="text-ui-accent font-bold">03. Кортіма CTF</li>
                        <li class="opacity-40">04. DAT</li>
                        <li class="opacity-40">05. Додаткові активності</li>
                    </ul>
                </div>
            </section>

            <section class="w-full md:w-1/2 md:self-end pb-64pt reveal">
                <h2 class="font-mono pb-16pt border-b border-ui-white/10">Скільки у мене вільного часу?</h2>
                <div class="pt-16pt">
                    <div class="flex items-baseline gap-8pt pb-8pt">
                        <span class="text-4xl md:text-6xl font-mono text-ui-accent">6</span>
                        <span class="text-xl font-mono opacity-30">/ 10</span>
                    </div>
                    <p>
                        Маю достатньо вільного часу, щоб взяти навантаження кортіми на себе. Я чудово усвідомлюю об'єм
                        роботи,
                        базуючись на досвіді LEoE, і я повністю готовий до цього темпу.
                    </p>
                </div>
            </section>

            <section class="w-full md:w-1/2 pb-96pt reveal">
                <h2 class="font-mono pb-16pt border-b border-ui-white/10 uppercase tracking-widest">Чому саме я?</h2>
                <p class="pt-16pt pb-24pt">
                    Який би ти вибір не зробив. Я поважатиму його.
                    Проте, якщо намагатись себе продати, то я вважаю цей мотиваційний лист - це вже доказ того що я
                    готовий навіть
                    на початковому етапі достатньо вкластись, щоб створити невеликий продукт.
                </p>
                <div
                    class="bg-ui-white/5 p-16pt border-l-2 border-ui-accent font-mono text-[11px] md:text-xs space-y-2pt ">
                    <p class="text-ui-accent">// Stack Trace:</p>
                    <p>Frontend: Vue.js + TailwindCSS [Host: GitHub Pages]</p>
                    <p>CI/CD: GitHub Actions [Automated Deploy]</p>
                    <p>Backend: FastAPI + JWT Auth [Host: Render.com]</p>
                    <p>Database: PostgreSQL [Managed by Neon.tech]</p>
                </div>


                <section class="reveal pt-32pt">


                    <a href="https://github.com/p-i-r-u-m/ctf2026_ml" target="_blank"
                        class="group block w-full border-[3px] border-ui-white/20 hover:border-ui-accent bg-ui-white/5 hover:bg-ui-accent/5 transition-all duration-300 p-16pt relative overflow-hidden">

                        <div
                            class="absolute top-0 right-0 p-4pt font-mono text-[10px] opacity-20 group-hover:opacity-100 group-hover:text-ui-accent transition-opacity">

                            [PDF]

                        </div>


                        <div class="flex items-center gap-24pt">

                            <div
                                class="w-64pt h-64pt bg-ui-white/10 flex items-center justify-center shrink-0 border border-ui-white/10 group-hover:border-ui-accent/30 transition-colors">

                                <svg class="w-32pt h-32pt opacity-40 group-hover:opacity-100 group-hover:text-ui-accent transition-all"
                                    fill="none" stroke="currentColor" viewBox="0 0 24 24">

                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"
                                        d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />

                                </svg>

                            </div>


                            <div class="font-mono">

                                <h3
                                    class="text-sm md:text-base mb-4pt uppercase tracking-wider group-hover:text-ui-accent transition-colors">

                                    ML_GITHUB

                                </h3>

                                <div class="text-[10px] opacity-50 flex flex-col gap-2pt">

                                    <span>FORMAT: LINK</span>

                                    <span
                                        class="text-ui-accent opacity-0 group-hover:opacity-100 transition-opacity">>>>
                                        CLICK TO

                                        OPEN</span>

                                </div>

                            </div>

                        </div>

                    </a>

                </section>
            </section>

            <section class="w-full md:w-2/3 md:self-end pb-96pt reveal">
                <h2 class="font-mono pb-16pt border-b border-ui-white/10 uppercase tracking-widest md:text-right">
                    Technical
                    Matrix</h2>

                <div class="grid grid-cols-2 md:grid-cols-4 gap-8pt pt-16pt font-mono text-[10px] uppercase">
                    <div class="border border-ui-white/20 p-8pt text-ui-accent">Linux / Arch / Fedora</div>
                    <div class="border border-ui-white/20 p-8pt text-ui-accent">Docker / Compose</div>
                    <div class="border border-ui-white/20 p-8pt">Python / FastAPI</div>
                    <div class="border border-ui-white/20 p-8pt">Networking / TCP/IP</div>
                    <div class="border border-ui-white/20 p-8pt ">Terraform / IaC</div>
                    <div class="border border-ui-white/20 p-8pt">AWS / Cloud Infrastructure</div>
                    <div class="border border-ui-white/20 p-8pt">Vue.js / Vite</div>
                    <div class="border border-ui-white/20 p-8pt">SQL / Postgres</div>
                    <div class="border border-ui-white/20 p-8pt text-ui-accent">Git / Actions</div>
                    <div class="border border-ui-white/20 p-8pt text-ui-accent">Figma / UI&UX</div>
                    <div class="border border-ui-white/20 p-8pt">Notion / Docs</div>
                    <div class="border border-ui-white/20 p-8pt">HTML / CSS</div>
                </div>

                <div class="mt-32pt flex flex-col md:flex-row gap-16pt">
                    <a href="https://github.com/p-i-r-u-m" target="_blank"
                        class="flex-1 border border-ui-white/10 p-12pt hover:border-ui-accent transition-colors flex justify-between items-center group">
                        <span class="font-mono text-xs">GitHub</span>
                        <span class="text-ui-accent opacity-0 group-hover:opacity-100">-></span>
                    </a>
                    <a href="https://www.credly.com/badges/b4190763-2d0d-4754-8abf-4751e0288b39/linked_in_profile"
                        target="_blank"
                        class="flex-1 border border-ui-white/10 p-12pt hover:border-ui-accent transition-colors flex justify-between items-center group">
                        <span class="font-mono text-xs">IBM Cloud Computing</span>
                        <span class="text-ui-accent opacity-0 group-hover:opacity-100">-></span>
                    </a>
                    <a href="https://drive.google.com/file/d/1d5ca_ZKdVuJ6aH_3dezieV5jIY0SE5nI/view?usp=sharing"
                        target="_blank"
                        class="flex-1 border border-ui-white/10 p-12pt hover:border-ui-accent transition-colors flex justify-between items-center group">
                        <span class="font-mono text-xs">Docker Fundamentals</span>
                        <span class="text-ui-accent opacity-0 group-hover:opacity-100">-></span>
                    </a>
                </div>
            </section>

            <section class="w-full md:w-1/2 pb-96pt reveal">
                <h2 class="font-mono pb-16pt border-b border-ui-white/10">Reflections & Integrity</h2>
                <div class="pt-16pt space-y-16pt">
                    <p>
                        Але, мабуть, основне. Це те, що моя мотивація – це забезпечити результат для свого ж
                        довгострокового успіху.
                        Я розглядаю кортіму CTF як ідеальний тренувальний полігон своїх хард- та софт-скілів для
                        досягнення вищої
                        фінансової незалежності у майбутньому.
                    </p>
                    <p class="text-ui-accent">
                        Я бестівець, який зміг вийти з вигорання від першої кортіми, та готовий йти далі, відкрито про
                        це говорити
                        та вказати навіть на чіткі патерни. Я вже знаю свої ліміти у роботі.
                    </p>
                </div>
            </section>

            <section class="w-full md:w-1/2 md:self-end pb-128pt reveal">
                <h2 class="font-mono pb-16pt border-b border-ui-white/10">UI/UX + Ecosystem Knowledge</h2>
                <p class="pt-16pt">
                    І наостанок: я був дизайнером LEoE, що для тебе як МО робить мене як підтримку для набраного
                    дизайнера у
                    кортімі та доводить, що я здатен забезпечити якісний UI/UX. Також я вважаю, що цей досвід дозволить
                    мені
                    бачити івент доволі цілісно, бо вже працював з LG, PR, CR.
                </p>
            </section>

            <Button to="/login">Content Responsible</Button>

        </main>

        <Footer></Footer>
    </div>
</template>