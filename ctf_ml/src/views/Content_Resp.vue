<script setup lang="ts">
import { onMounted, ref } from 'vue'
import logo from "../assets/logo.svg";
import Footer from "../components/Footer.vue";
import Button from '../components/Button.vue'

const sections = ref<HTMLElement[]>([]);

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
      <p>Content Responsible</p>
    </header>

    <main class="grow flex flex-col">
      <h2 class="font-mono">I wanna be</h2>
      <h1 class="font-mono text-ui-accent pb-96pt uppercase tracking-tighter">Content Responsible</h1>

      <section class="w-full md:w-1/2 pb-64pt reveal">
        <h2 class="font-mono pb-16pt border-b border-ui-white/10">Хто я?</h2>
        <p class="pt-16pt">
          Привіт! Уявімо, що ти мене ніколи не бачив. Хто ж я такий? Яким чином мене можна описати? Та що вказує на мою
          готовність та мотивацію стати членом кортіми CTF.
        </p>
      </section>

      <section class="w-full md:w-1/2 md:self-end pb-64pt reveal">
        <h2 class="font-mono pb-16pt border-b border-ui-white/10">Чому саме CTF?</h2>
        <p class="pt-16pt">
          Цікаве питання, на яке, мабуть, дуже дивно відповідати щось типу “тому що я обожнюю та люблю його”. Я не знаю.
          Поки що. Я сподіваюсь, що я полюблю CTF усім серцем і це буде неймовірний досвід, проте наразі я можу пояснити
          це лише прагматично.
          У BEST великий вибір подач у кортіми. Але не всі із них – технічні, та дозволяють створити щось в айтішній
          сфері, яка мені подобається. CTF дозволяє мені отримати досвід налагодження технічної інфраструктури івенту,
          щоб цим користувалось потім декілька десятків людей.
        </p>
      </section>

      <section class="w-full md:w-1/2 pb-64pt reveal">
        <h2 class="font-mono pb-16pt border-b border-ui-white/10">Чому я хочу бути контентом?</h2>
        <p class="pt-16pt">
          Все доволі просто. Я хочу стати DevOps-інженером. Я впевнений, що ти в курсі: щоб пробитись на таку не
          entry-level роботу, треба мати досвід. Організація CTF може стати саме таким початковим досвідом, і посада
          контента CTF – найбільш наближена за досвідом до цієї професії. Твоя історія – для мене доказ, що цей шлях має
          сенс.
        </p>
      </section>

      <section class="w-full md:w-1/2 md:self-end pb-96pt reveal">
        <h2 class="font-mono pb-16pt border-b border-ui-white/10">Мій бекграунд</h2>
        <p class="pt-16pt pb-32pt">
          У організації CTF-змагань ні. У проходженні – так. Я цікавився деякий час кібербезпекою і навіть думав
          поступити на цю спеціальність. За цей час я встиг спробувати поклацати такі платформи, як HackTheBox, picoCTF,
          та навіть брав участь в одних CTF-змаганнях, організованих Маріупольським університетом, які були у форматі
          Jeopardy.
        </p>

        <section class="reveal">


          <a href="https://drive.google.com/file/d/1COYt0R7lptTXdkpRDaf2y8FMN7b3lXGM/view?usp=sharing" target="_blank"
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

                  <span class="text-ui-accent opacity-0 group-hover:opacity-100 transition-opacity">>>> CLICK TO

                    OPEN</span>

                </div>

              </div>

            </div>

          </a>

        </section>
      </section>


      <section class="w-full md:w-1/2 pb-32pt reveal">
        <h2 class="font-mono pb-16pt border-b border-ui-white/10">Мій погляд на контент CTF?</h2>
        <p class="pt-16pt">
          Прочитавши твій Action Plan, я повністю підтримую перехід до King of the Hill. Це формат, який дає учасникам
          реальний драйв, а нам – можливість вийти за рамки звичних тасок. Твій фокус на використанні функціоналу
          наявної платформи – це найраціональніший шлях.
        </p>
      </section>

      <section class="w-full md:w-1/2 md:self-end pb-64pt reveal">
        <p class="pt-16pt">
          Я наразі не знаю яка платформа для цього найкраща, варто зробити дослідження під час кортіми яку платформу
          розгорнути, щоб делегувати контроль балів та візуального інтерфейсу на існуючий open-source проєкт. Проте я
          пропоную відійти від важких віртуальних машин на користь контейнеризованої інфраструктури. Це дозволить нам
          вирішити ризик відсутності великих ресурсів та забезпечити стабільність. До того ж контейнеризація дозволяє
          швидше та легше реагувати на інциденти, якщо інфраструктура ляже від навантажень під час івенту.
        </p>
      </section>


      <section class="w-full pb-96pt reveal">
        <div class="border-l-4 border-ui-accent pl-24pt">
          <h2 class="font-mono uppercase mb-32pt">
            Vision: <span class="text-ui-accent">Chained KotH</span>
          </h2>
          <p class="max-w-3xl opacity-90">
            Я пропоную відійти від формату однієї статичної «гори» для всіх. Моє бачення – це мережа взаємопов'язаних
            вузлів. Це дозволяє реалізувати Lateral Movement, що є стандартом реальних кібератак, та забезпечити високу
            складність без зайвого технічного перевантаження.
          </p>
        </div>
      </section>



      <section class="grid grid-cols-1 md:grid-cols-2 gap-64pt pb-96pt">

        <div class="reveal">
          <h3 class="font-mono text-ui-accent pb-8pt uppercase text-sm">// Active Service</h3>
          <p class="text-sm">
            “Гора” – це не просто текстовий файл для запису назви команди. Це запущений вебзастосунок чи база даних.
            Бали нараховуються лише за умови, що сервіс залишається активним та доступним під контролем команди. Це
            змушує учасників не просто захопити рут, а грамотно патчити вразливості, щоб не покласти систему самому.
          </p>
        </div>

        <div class="reveal md:mt-32pt">
          <h3 class="font-mono text-ui-accent pb-8pt uppercase text-sm">// Chained architecture</h3>
          <p class="text-sm">
            Учасники потрапляють на наступну, складнішу «гору» лише після захоплення попередньої. Це створює природний
            фільтр складності та підтримує інтерес до кінця івенту.
          </p>
        </div>

        <div class="reveal md:mt-32pt">
          <h3 class="font-mono text-ui-accent pb-8pt uppercase text-sm">// Team Dynamics</h3>
          <p class="text-sm">
            Ідеально для команд по 3-4 людини: один тримає оборону поточної цілі, другий проводить розвідку
            наступної, третій шукає приховані прапорці.
          </p>
        </div>

        <div class="reveal">
          <h3 class="font-mono text-ui-accent pb-8pt uppercase text-sm">// Hybrid KotH + Jeopardy</h3>
          <p class="text-sm pb-16pt">
            Щоб уникнути ситуації, коли одна сильна команда зацементувала першу гору і зупинила гру, я пропоную додати
            всередину кожної гори приховані прапорці.
          </p>
          <p class="text-sm pb-8pt">
            Цар гори отримує стабільний пасивний дохід балів за утримання.
          </p>

          <p class="text-sm">
            Претенденти можуть збирати прапорці всередині системи, що дає їм швидкий буст балів.
            Це створює постійну напругу: лідер змушений або масштабуватись на наступну гору (щоб отримувати більше), або
            відволікатись на пошук прапорців, щоб його не обігнали конкуренти за рахунок луту.
          </p>
        </div>


      </section>

      <section class="w-full pb-64pt reveal text-center">
        <p class="font-mono text-xs opacity-40 mb-16pt">MY_VISION</p>
        <h2 class="text-2xl md:text-4xl font-mono uppercase italic">
          Чому це <span class="text-ui-accent">вигідно</span> для івенту?
        </h2>
      </section>

      <section class="grid grid-cols-1 md:grid-cols-3 gap-32pt md:gap-64pt pb-128pt reveal">

        <div class="border-t border-ui-white/10 pt-16pt">
          <h3 class="font-mono text-ui-accent uppercase text-xs mb-8pt">// Технічний ризик</h3>
          <p class="text-xs md:text-sm opacity-80 leading-relaxed">
            Вирішення технічного ризику: Використання Docker замість важких віртуалок дозволяє нам легко розгорнути таку
            архітектуру та забезпечити швидкий ресет вузлів у разі інцидентів.
          </p>
        </div>

        <div class="border-t border-ui-white/10 pt-16pt">
          <h3 class="font-mono text-ui-accent uppercase text-xs mb-8pt">// Динаміка</h3>
          <p class="text-xs md:text-sm opacity-80 leading-relaxed">
            Командна динаміка: Це ідеальний виклик для команд по 3-4 людини, де кожен матиме свою роль: оборона поточної
            гори, розвідка наступної та пошук прапорців.
          </p>
        </div>

        <div class="border-t border-ui-white/10 pt-16pt">
          <h3 class="font-mono text-ui-accent uppercase text-xs mb-8pt">// Ресурс контенту</h3>
          <p class="text-xs md:text-sm opacity-80 leading-relaxed">
            Наповнення контентом: Такий підхід дозволяє нам перевикористовувати прапорці просто з різними патернами
            знаходження на кожній горі, тим самим зберігши ресурс топік-тімки, забезпечивши якість.
          </p>
        </div>

      </section>


      <section class="w-full md:w-1/2 md:self-end pb-64pt reveal">
        <h2 class="font-mono pb-16pt border-b border-ui-white/10">Мої плани на 6 місяців</h2>
        <p class="pt-16pt">
          Я планую залишатися у Львові: навчання в університеті, робота, можливо — пошук нових викликів. Мій графік
          стабільний, тому я буду відкритий та доступний для кортіми більшу частину часу протягом усього періоду
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
            Маю достатньо вільного часу, щоб взяти навантаження кортіми на себе. Я чудово усвідомлюю об'єм роботи,
            базуючись на досвіді LEoE, і я повністю готовий до цього темпу.
          </p>
        </div>
      </section>

      <section class="w-full md:w-1/2 pb-96pt reveal">
        <h2 class="font-mono pb-16pt border-b border-ui-white/10 uppercase tracking-widest">Чому саме я?</h2>
        <p class="pt-16pt pb-24pt">
          Який би ти вибір не зробив. Я поважатиму його.
          Проте, якщо намагатись себе продати, то я вважаю цей мотиваційний лист - це вже доказ того що я готовий навіть
          на початковому етапі достатньо вкластись, щоб створити невеликий продукт.
        </p>
        <div class="bg-ui-white/5 p-16pt border-l-2 border-ui-accent font-mono text-[11px] md:text-xs space-y-2pt ">
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

                  <span class="text-ui-accent opacity-0 group-hover:opacity-100 transition-opacity">>>> CLICK TO

                    OPEN</span>

                </div>

              </div>

            </div>

          </a>

        </section>
      </section>

      <section class="w-full md:w-2/3 md:self-end pb-96pt reveal">
        <h2 class="font-mono pb-16pt border-b border-ui-white/10 uppercase tracking-widest md:text-right">Technical
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
          <a href="https://www.credly.com/badges/b4190763-2d0d-4754-8abf-4751e0288b39/linked_in_profile" target="_blank"
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
            Але, мабуть, основне. Це те, що моя мотивація – це забезпечити результат для свого ж довгострокового успіху.
            Я розглядаю кортіму CTF як ідеальний тренувальний полігон своїх хард- та софт-скілів для досягнення вищої
            фінансової незалежності у майбутньому.
          </p>
          <p class="text-ui-accent">
            Я бестівець, який зміг вийти з вигорання від першої кортіми, та готовий йти далі, відкрито про це говорити
            та вказати навіть на чіткі патерни. Я вже знаю свої ліміти у роботі.
          </p>
        </div>
      </section>

      <section class="w-full md:w-1/2 md:self-end pb-128pt reveal">
        <h2 class="font-mono pb-16pt border-b border-ui-white/10">UI/UX + Ecosystem Knowledge</h2>
        <p class="pt-16pt">
          І наостанок: я був дизайнером LEoE, що для тебе як МО робить мене як підтримку для набраного дизайнера у
          кортімі та доводить, що я здатен забезпечити якісний UI/UX. Також я вважаю, що цей досвід дозволить мені
          бачити івент доволі цілісно, бо вже працював з LG, PR, CR.
        </p>
      </section>

      <Button to="/it_resp">IT Responsible</Button>

    </main>

    <Footer></Footer>
  </div>
</template>