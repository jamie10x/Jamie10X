<div align="center">
  <img src="./jamie10x-os.svg" alt="Jamie10X OS" width="100%"/>
</div>

<br/>

<div align="center">

| `SYSTEM` | `VALUE` | `SYSTEM` | `VALUE` |
|:---|:---|:---|:---|
| **Status** | 🟢 Building Android apps | **Primary Stack** | Kotlin + Jetpack Compose |
| **Cross-Platform** | Flutter / Dart | **Backend & Web** | TypeScript · Go · Python |
| **Focus** | Clean Architecture · Performance · UX | **Timezone** | UTC+5 |

</div>

<br/>

<div align="center">
  <a href="https://linkedin.com/in/jamshidbek-boynazarov-956227248">
    <img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=flat-square&logo=linkedin&logoColor=white" alt="LinkedIn"/>
  </a>
  &nbsp;
  <a href="https://github.com/Jamie10X">
    <img src="https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white" alt="GitHub"/>
  </a>
  &nbsp;
  <a href="mailto:jamshidboynazarov0@gmail.com">
    <img src="https://img.shields.io/badge/Email-D14836?style=flat-square&logo=gmail&logoColor=white" alt="Email"/>
  </a>
  &nbsp;
  <img src="https://komarev.com/ghpvc/?username=Jamie10X&color=3DDC84&style=flat-square&label=PROFILE+VIEWS" alt="Profile Views"/>
</div>

---

## `>_ jamie10x@github`

```bash
jamie10x@github:~$ whoami
Android Developer focused on Kotlin, Java, Jetpack Compose and clean architecture.
Builds production-ready mobile apps with great UX, tight performance, and scalable code.

jamie10x@github:~$ build-modes
native-android     →  production-ready mobile apps with Jetpack Compose & MVVM/MVI
flutter            →  cross-platform mobile apps with Dart & Firebase
web-backend        →  REST APIs, Node.js, TypeScript, Go, Python
problem-solving    →  algorithms, architecture design, product thinking
```

---

## Featured Builds

| Project | What I Built | Stack |
|:---|:---|:---|
| `native-android-app` | <!-- Replace: full-featured Android app with offline support --> | Kotlin · Compose · Room · Hilt |
| `flutter-cross-platform` | <!-- Replace: cross-platform mobile app for iOS & Android --> | Flutter · Dart · Firebase |
| `backend-api-project` | <!-- Replace: REST API with auth and database integration --> | Go · TypeScript · Node.js · MongoDB |

---

## Tech Stack

#### Native Android
![Kotlin](https://img.shields.io/badge/Kotlin-7F52FF?style=flat-square&logo=kotlin&logoColor=white)
![Java](https://img.shields.io/badge/Java-ED8B00?style=flat-square&logo=openjdk&logoColor=white)
![Jetpack Compose](https://img.shields.io/badge/Jetpack_Compose-4285F4?style=flat-square&logo=jetpackcompose&logoColor=white)
![XML Layouts](https://img.shields.io/badge/XML_Layouts-3DDC84?style=flat-square&logo=android&logoColor=white)
![Material Design](https://img.shields.io/badge/Material_Design-757575?style=flat-square&logo=materialdesign&logoColor=white)
![Coroutines](https://img.shields.io/badge/Coroutines-7F52FF?style=flat-square&logo=kotlin&logoColor=white)
![Flow](https://img.shields.io/badge/Flow-7F52FF?style=flat-square&logo=kotlin&logoColor=white)
![Room](https://img.shields.io/badge/Room-3DDC84?style=flat-square&logo=android&logoColor=white)
![Retrofit](https://img.shields.io/badge/Retrofit-48B983?style=flat-square&logo=square&logoColor=white)
![DataStore](https://img.shields.io/badge/DataStore-4285F4?style=flat-square&logo=android&logoColor=white)
![WorkManager](https://img.shields.io/badge/WorkManager-3DDC84?style=flat-square&logo=android&logoColor=white)
![Navigation](https://img.shields.io/badge/Navigation-4285F4?style=flat-square&logo=android&logoColor=white)
![Paging 3](https://img.shields.io/badge/Paging_3-7F52FF?style=flat-square&logo=android&logoColor=white)
![Hilt](https://img.shields.io/badge/Hilt-3DDC84?style=flat-square&logo=dagger&logoColor=white)
![Koin](https://img.shields.io/badge/Koin-7F52FF?style=flat-square&logo=kotlin&logoColor=white)

#### Cross-Platform
![Flutter](https://img.shields.io/badge/Flutter-02569B?style=flat-square&logo=flutter&logoColor=white)
![Dart](https://img.shields.io/badge/Dart-0175C2?style=flat-square&logo=dart&logoColor=white)
![Firebase](https://img.shields.io/badge/Firebase-FFCA28?style=flat-square&logo=firebase&logoColor=black)

#### Web & Backend
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black)
![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white)
![Go](https://img.shields.io/badge/Go-00ADD8?style=flat-square&logo=go&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Node.js](https://img.shields.io/badge/Node.js-339933?style=flat-square&logo=nodedotjs&logoColor=white)
![REST APIs](https://img.shields.io/badge/REST_APIs-FF6C37?style=flat-square&logo=postman&logoColor=white)
![MongoDB](https://img.shields.io/badge/MongoDB-4EA94B?style=flat-square&logo=mongodb&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-4479A1?style=flat-square&logo=postgresql&logoColor=white)

#### Tools
![Git](https://img.shields.io/badge/Git-F05033?style=flat-square&logo=git&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=flat-square&logo=githubactions&logoColor=white)
![Postman](https://img.shields.io/badge/Postman-FF6C37?style=flat-square&logo=postman&logoColor=white)
![Figma](https://img.shields.io/badge/Figma-F24E1E?style=flat-square&logo=figma&logoColor=white)

---

## Architecture Fingerprint

```mermaid
flowchart LR
    UI["🖥️ UI\nCompose / Flutter"] --> VM["⚙️ ViewModel\nState + Events"]
    VM --> UC["🧩 Use Cases\nBusiness Logic"]
    UC --> Repo["📦 Repository\nSingle Source of Truth"]
    Repo --> API["🌐 Remote\nRetrofit / REST"]
    Repo --> DB["💾 Local\nRoom / DataStore"]

    style UI fill:#3DDC84,color:#0B0F14,stroke:#3DDC84
    style VM fill:#4285F4,color:#fff,stroke:#4285F4
    style UC fill:#7F52FF,color:#fff,stroke:#7F52FF
    style Repo fill:#1E2D3D,color:#E6EDF3,stroke:#4B5563
    style API fill:#0d1a2a,color:#3DDC84,stroke:#3DDC84
    style DB fill:#0d1a2a,color:#4285F4,stroke:#4285F4
```

---

## Currently Syncing

*Auto-updating with the latest from the Android Developers Blog.*

<!--START_SECTION:learn-->
#### 📖 [How FotMob leveraged cross-device discovery to score record Wear OS adoption](https://android-developers.googleblog.com/2026/05/fotmob-wear-os-adoption-cross-device-discovery.html)
<!--END_SECTION:learn-->

---

## Stats & Activity

<div align="center">

  <a href="https://github.com/anuraghazra/github-readme-stats">
    <img alt="GitHub Stats" src="https://github-readme-stats.vercel.app/api?username=Jamie10X&show_icons=true&theme=tokyonight&hide_border=true&include_all_commits=true&count_private=true"/>
  </a>

  <a href="https://github.com/anuraghazra/github-readme-stats">
    <img alt="Top Languages" src="https://github-readme-stats.vercel.app/api/top-langs/?username=Jamie10X&layout=compact&theme=tokyonight&hide_border=true&include_all_commits=true&count_private=true"/>
  </a>

  <a href="https://github.com/vn7n24fzkq/github-profile-summary-cards">
    <img alt="Productive Time" src="https://github-profile-summary-cards.vercel.app/api/cards/productive-time?username=Jamie10X&theme=tokyonight&utc_offset=+5"/>
  </a>

  <a href="https://github.com/ashutosh00710/github-readme-activity-graph">
    <img alt="Activity Graph" src="https://github-readme-activity-graph.vercel.app/graph?username=Jamie10X&bg_color=1a1b27&color=c0caf5&line=3DDC84&point=4285F4&area=true&hide_border=true"/>
  </a>

</div>

---

## Coding Profiles

<div align="center">
  <a href="https://www.leetcode.com/Jamie1023">
    <img alt="LeetCode" src="https://img.shields.io/badge/LeetCode-000000?style=for-the-badge&logo=LeetCode&logoColor=%23d16c06"/>
  </a>
  &nbsp;
  <a href="https://www.hackerrank.com/jamshidboynazar1">
    <img alt="HackerRank" src="https://img.shields.io/badge/HackerRank-2EC866?style=for-the-badge&logo=HackerRank&logoColor=white"/>
  </a>
  &nbsp;
  <a href="https://developers.google.com/profile/u/JamshidbekBoynazarov">
    <img alt="Google Developer" src="https://img.shields.io/badge/Google_Dev-4285F4?style=for-the-badge&logo=google&logoColor=white"/>
  </a>
</div>

---

<div align="center">
  <sub>Open to Android, Flutter, and backend collaboration.</sub>
</div>
