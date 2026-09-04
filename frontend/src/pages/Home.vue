<template>
  <div class="school-page">
    <!-- Top contact bar -->
    <div class="topbar">
      <div class="page-container topbar-inner">
        <div class="top-contact">
          <span>☎ +91 98765 43210</span>
          <span class="separator">|</span>
          <span>✉ info@yourschool.edu</span>
        </div>

        <div class="top-links">
          <a href="/app/desk">Parents Portal</a>
          <span>|</span>
          <a href="/app/desk">Students Portal</a>
          <span>|</span>
          <a href="#" aria-label="Facebook">f</a>
          <a href="#" aria-label="Instagram">◎</a>
          <a href="#" aria-label="YouTube">▶</a>
        </div>
      </div>
    </div>

    <!-- Main navigation -->
    <header class="navbar">
      <div class="page-container nav-inner">
        <a class="brand" href="#home">
          <div class="brand-logo">
            <span>YS</span>
          </div>
          <div>
            <div class="brand-name">Morpho SCHOOL</div>
            <div class="brand-tagline">LEARN · GROW · EXCEL</div>
          </div>
        </a>

        <button class="mobile-menu" @click="mobileOpen = !mobileOpen" aria-label="Toggle menu">
          <span></span><span></span><span></span>
        </button>

        <nav :class="['nav-links', { open: mobileOpen }]">
          <a class="active" href="#home" @click="mobileOpen = false">Home</a>
          <a href="#about" @click="mobileOpen = false">About Us</a>
          <a href="#academics" @click="mobileOpen = false">Academics</a>
          <a href="#admissions" @click="mobileOpen = false">Admissions</a>
          <a href="#campus" @click="mobileOpen = false">Campus Life</a>
          <a href="#gallery" @click="mobileOpen = false">Gallery</a>
          <a href="#contact" @click="mobileOpen = false">Contact</a>
          <a class="nav-cta" href="#contact" @click="mobileOpen = false">Enquire Now</a>
        </nav>
      </div>
    </header>

    <!-- Hero -->
    <section id="home" class="hero">
      <div class="hero-overlay"></div>
      <div class="page-container hero-content">
        <div class="hero-copy">
          <div class="eyebrow light">WELCOME TO YOUR SCHOOL</div>
          <h1>Inspiring Minds.<br />Shaping Futures.</h1>
          <p>
            Nurturing young minds through quality education,
            values, and real-world learning.
          </p>

          <div class="hero-actions">
            <a class="btn btn-orange" href="#admissions">Admissions Open 2026–27</a>
            <button class="btn btn-outline" @click="showVideo = true">
              <span class="play-icon">▶</span> Watch Video
            </button>
          </div>
        </div>
      </div>
    </section>

    <!-- Stats -->
    <section class="stats-wrap">
      <div class="page-container">
        <div class="stats">
          <div v-for="stat in stats" :key="stat.label" class="stat">
            <div class="stat-icon" v-html="stat.icon"></div>
            <div>
              <strong>{{ stat.value }}</strong>
              <span>{{ stat.label }}</span>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Four highlight cards -->
    <section id="academics" class="highlights page-container">
      <article v-for="item in highlights" :key="item.title" class="highlight-card">
        <div class="highlight-icon" v-html="item.icon"></div>
        <h3>{{ item.title }}</h3>
        <p>{{ item.description }}</p>
      </article>
    </section>

    <!-- About -->
    <section id="about" class="about section">
      <div class="page-container about-grid">
        <div class="about-copy">
          <div class="eyebrow">WELCOME TO OUR SCHOOL</div>
          <h2>A Place Where Every Child Can Shine</h2>
          <p>
            We provide a safe, supportive, and stimulating environment
            where students learn, grow, and become the best version of themselves.
          </p>
          <p>
            Our learning experience combines academic excellence with
            creativity, character, sports, technology, and leadership.
          </p>

          <div class="about-points">
            <div>✓ Experienced and caring teachers</div>
            <div>✓ Student-focused learning</div>
            <div>✓ Modern campus and facilities</div>
          </div>

          <a href="#contact" class="btn btn-navy">Learn More About Us</a>
        </div>

        <div class="about-images">
          <div class="about-main-image image-card">
            <img :src="images.school" alt="School campus" />
          </div>
          <div class="about-side-images">
            <div class="image-card">
              <img :src="images.classroom" alt="Students in classroom" />
            </div>
            <div class="image-card">
              <img :src="images.lab" alt="Students in science laboratory" />
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Academic programs -->
    <section class="section soft-bg">
      <div class="page-container">
        <div class="section-heading">
          <div class="eyebrow">ACADEMICS</div>
          <h2>Learning for Every Stage</h2>
          <p>Strong foundations, meaningful learning, and preparation for the future.</p>
        </div>

        <div class="programs">
          <article v-for="program in programs" :key="program.title" class="program-card">
            <div class="program-number">{{ program.number }}</div>
            <div>
              <h3>{{ program.title }}</h3>
              <p>{{ program.description }}</p>
            </div>
            <a href="#contact">Explore →</a>
          </article>
        </div>
      </div>
    </section>

    <!-- Campus -->
    <section id="campus" class="section">
      <div class="page-container">
        <div class="section-heading">
          <div class="eyebrow">CAMPUS LIFE</div>
          <h2>More Than a Classroom</h2>
          <p>A vibrant campus where students learn, create, play, and lead.</p>
        </div>

        <div class="campus-grid">
          <div v-for="facility in facilities" :key="facility.title" class="facility">
            <img :src="facility.image" :alt="facility.title" />
            <div class="facility-overlay">
              <span>{{ facility.title }}</span>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Admissions -->
    <section id="admissions" class="admission-banner">
      <div class="page-container admission-inner">
        <div>
          <div class="eyebrow light">ADMISSIONS</div>
          <h2>Give Your Child a Brighter Future</h2>
          <p>Admissions are now open for the 2026–27 academic year.</p>
        </div>
        <a class="btn btn-orange" href="#contact">Start Admission Process</a>
      </div>
    </section>

    <!-- Gallery -->
    <section id="gallery" class="section soft-bg">
      <div class="page-container">
        <div class="section-heading">
          <div class="eyebrow">GALLERY</div>
          <h2>Life at Your School</h2>
        </div>

        <div class="gallery-grid">
          <img v-for="image in gallery" :key="image.src" :src="image.src" :alt="image.alt" />
        </div>
      </div>
    </section>

    <!-- Contact -->
    <section id="contact" class="section">
      <div class="page-container contact-grid">
        <div class="contact-copy">
          <div class="eyebrow">GET IN TOUCH</div>
          <h2>We'd Love to Hear From You</h2>
          <p>
            Contact our admissions team for information about programs,
            campus visits, fees, and the admission process.
          </p>

          <div class="contact-details">
            <div>
              <strong>Address</strong>
              <span>123 Education Road, Bengaluru, Karnataka, India</span>
            </div>
            <div>
              <strong>Phone</strong>
              <span>+91 98765 43210</span>
            </div>
            <div>
              <strong>Email</strong>
              <span>info@yourschool.edu</span>
            </div>
          </div>
        </div>

        <form class="enquiry-card" @submit.prevent="submitEnquiry">
          <h3>Enquire Now</h3>

          <label>
            Parent Name
            <input v-model="form.name" type="text" placeholder="Enter your name" required />
          </label>

          <label>
            Phone Number
            <input v-model="form.phone" type="tel" placeholder="+91 XXXXX XXXXX" required />
          </label>

          <label>
            Email
            <input v-model="form.email" type="email" placeholder="you@example.com" required />
          </label>

          <label>
            Message
            <textarea v-model="form.message" rows="4" placeholder="How can we help?"></textarea>
          </label>

          <button class="btn btn-navy full" type="submit">Send Enquiry</button>

          <div v-if="submitted" class="success-message">
            Thank you! Your enquiry has been received.
          </div>
        </form>
      </div>
    </section>

    <!-- Footer -->
    <footer>
      <div class="page-container footer-grid">
        <div>
          <div class="footer-brand">YOUR SCHOOL</div>
          <p>Learn · Grow · Excel</p>
          <p class="muted">
            Inspiring young minds through quality education,
            strong values, and meaningful experiences.
          </p>
        </div>

        <div>
          <h4>Quick Links</h4>
          <a href="#about">About Us</a>
          <a href="#academics">Academics</a>
          <a href="#admissions">Admissions</a>
          <a href="#campus">Campus Life</a>
        </div>

        <div>
          <h4>Portals</h4>
          <a href="/app/desk">Parents Portal</a>
          <a href="/app/desk">Students Portal</a>
          <a href="/app/desk">Teacher Portal</a>
          <a href="/app/desk">School  Login</a>
        </div>

        <div>
          <h4>Contact</h4>
          <p class="muted">+91 98765 43210</p>
          <p class="muted">info@yourschool.edu</p>
          <p class="muted">Bengaluru, Karnataka</p>
        </div>
      </div>

      <div class="copyright">
        © {{ new Date().getFullYear() }} Your School. All Rights Reserved.
      </div>
    </footer>

    <!-- Video modal -->
    <div v-if="showVideo" class="modal-backdrop" @click.self="showVideo = false">
      <div class="video-modal">
        <button class="close-modal" @click="showVideo = false">×</button>
        <div class="video-placeholder">
          <div class="big-play">▶</div>
          <h3>School Introduction Video</h3>
          <p>Replace this area with your YouTube/Vimeo/Frappe video.</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const mobileOpen = ref(false)
const showVideo = ref(false)
const submitted = ref(false)

const form = ref({
  name: '',
  phone: '',
  email: '',
  message: ''
})

/*
 * Replace these image URLs with your Frappe File URLs.
 * Example:
 * /files/school-campus.jpg
 */
const images = {
  school: 'https://images.unsplash.com/photo-1562774053-701939374585?auto=format&fit=crop&w=1200&q=85',
  classroom: 'https://images.unsplash.com/photo-1509062522246-3755977927d7?auto=format&fit=crop&w=900&q=85',
  lab: 'https://images.unsplash.com/photo-1532094349884-543bc11b234d?auto=format&fit=crop&w=900&q=85'
}

const stats = [
  {
    value: '25+',
    label: 'Years of Excellence',
    icon: '🎓'
  },
  {
    value: '1200+',
    label: 'Students',
    icon: '♧'
  },
  {
    value: '80+',
    label: 'Expert Teachers',
    icon: '♙'
  },
  {
    value: '15+',
    label: 'Awards Won',
    icon: '🏆'
  }
]

const highlights = [
  {
    title: 'Academics',
    description: 'CBSE curriculum with modern teaching methods.',
    icon: '📖'
  },
  {
    title: 'Achievements',
    description: 'Recognizing talent and encouraging excellence.',
    icon: '🏆'
  },
  {
    title: 'Sports',
    description: 'Building strength, teamwork, and leadership.',
    icon: '⚽'
  },
  {
    title: 'Values',
    description: 'Shaping responsible and compassionate citizens.',
    icon: '♡'
  }
]

const programs = [
  {
    number: '01',
    title: 'Primary School',
    description: 'Strong foundations through curiosity, creativity, and joyful learning.'
  },
  {
    number: '02',
    title: 'Middle School',
    description: 'Developing critical thinking, confidence, and independent learning.'
  },
  {
    number: '03',
    title: 'Secondary School',
    description: 'Preparing students for board examinations, higher education, and life.'
  }
]

const facilities = [
  {
    title: 'Modern Classrooms',
    image: 'https://images.unsplash.com/photo-1509062522246-3755977927d7?auto=format&fit=crop&w=1000&q=85'
  },
  {
    title: 'Science Laboratory',
    image: 'https://images.unsplash.com/photo-1532094349884-543bc11b234d?auto=format&fit=crop&w=1000&q=85'
  },
  {
    title: 'Library',
    image: 'https://images.unsplash.com/photo-1507842217343-583bb7270b66?auto=format&fit=crop&w=1000&q=85'
  },
  {
    title: 'Sports Ground',
    image: 'https://images.unsplash.com/photo-1461896836934-ffe607ba8211?auto=format&fit=crop&w=1000&q=85'
  }
]

const gallery = [
  {
    src: images.school,
    alt: 'School campus'
  },
  {
    src: images.classroom,
    alt: 'Classroom'
  },
  {
    src: images.lab,
    alt: 'Science laboratory'
  },
  {
    src: 'https://images.unsplash.com/photo-1461896836934-ffe607ba8211?auto=format&fit=crop&w=1000&q=85',
    alt: 'Sports'
  },
  {
    src: 'https://images.unsplash.com/photo-1507842217343-583bb7270b66?auto=format&fit=crop&w=1000&q=85',
    alt: 'Library'
  },
  {
    src: 'https://images.unsplash.com/photo-1529390079861-591de354faf5?auto=format&fit=crop&w=1000&q=85',
    alt: 'Students'
  }
]

function submitEnquiry() {
  submitted.value = true

  // Later, replace this with a Frappe API call.
  // Example endpoint:
  // /api/resource/Website School Enquiry
  //
  // frappe.call({
  //   method: 'frappe.client.insert',
  //   args: {
  //     doc: {
  //       doctype: 'Website School Enquiry',
  //       parent_name: form.value.name,
  //       phone: form.value.phone,
  //       email: form.value.email,
  //       message: form.value.message
  //     }
  //   }
  // })

  form.value = {
    name: '',
    phone: '',
    email: '',
    message: ''
  }
}
</script>

<style scoped>
:global(*) {
  box-sizing: border-box;
}

:global(html) {
  scroll-behavior: smooth;
}

:global(body) {
  margin: 0;
  font-family:
    Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont,
    "Segoe UI", sans-serif;
  color: #18202b;
  background: #fff;
}

:global(a) {
  text-decoration: none;
  color: inherit;
}

:global(button),
:global(input),
:global(textarea) {
  font: inherit;
}

.school-page {
  --navy: #0d2344;
  --navy-dark: #081a34;
  --orange: #ef7424;
  --orange-light: #fff3ea;
  --text: #1a2029;
  --muted: #6d7480;
  --border: #e7e8eb;
  --soft: #f7f8fa;
  overflow-x: hidden;
}

.page-container {
  width: min(1160px, calc(100% - 48px));
  margin: 0 auto;
}

/* Top bar */
.topbar {
  background: var(--navy);
  color: #fff;
  font-size: 12px;
}

.topbar-inner {
  min-height: 38px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.top-contact,
.top-links {
  display: flex;
  align-items: center;
  gap: 10px;
}

.top-links a {
  opacity: 0.95;
}

.top-links a:hover {
  color: #ffb27f;
}

.separator {
  opacity: 0.45;
}

/* Navbar */
.navbar {
  position: sticky;
  top: 0;
  z-index: 50;
  background: rgba(255, 255, 255, 0.97);
  backdrop-filter: blur(10px);
  border-bottom: 1px solid #eee;
}

.nav-inner {
  min-height: 84px;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.brand {
  display: flex;
  align-items: center;
  gap: 12px;
}

.brand-logo {
  width: 50px;
  height: 50px;
  border: 3px solid var(--navy);
  border-radius: 50% 50% 45% 45%;
  display: grid;
  place-items: center;
  color: var(--orange);
  font-weight: 900;
  font-size: 13px;
  position: relative;
}

.brand-logo::before {
  content: "";
  position: absolute;
  inset: -6px;
  border-left: 2px solid var(--orange);
  border-right: 2px solid var(--orange);
  border-radius: 50%;
  transform: rotate(-15deg);
}

.brand-name {
  color: var(--navy);
  font-weight: 800;
  letter-spacing: 0.6px;
  font-size: 17px;
}

.brand-tagline {
  color: #777;
  font-size: 9px;
  letter-spacing: 1.3px;
  margin-top: 2px;
}

.nav-links {
  display: flex;
  align-items: center;
  gap: 27px;
  font-size: 13px;
  font-weight: 600;
}

.nav-links a {
  position: relative;
  padding: 31px 0;
  white-space: nowrap;
}

.nav-links a:not(.nav-cta)::after {
  content: "";
  position: absolute;
  left: 0;
  right: 0;
  bottom: 22px;
  height: 2px;
  background: var(--orange);
  transform: scaleX(0);
  transition: transform 0.2s;
}

.nav-links a:hover::after,
.nav-links a.active::after {
  transform: scaleX(1);
}

.nav-cta {
  background: var(--navy);
  color: #fff !important;
  padding: 12px 19px !important;
  border-radius: 7px;
}

.nav-cta:hover {
  background: var(--orange);
}

.mobile-menu {
  display: none;
  border: 0;
  background: transparent;
  padding: 8px;
  cursor: pointer;
}

.mobile-menu span {
  display: block;
  width: 25px;
  height: 2px;
  margin: 5px 0;
  background: var(--navy);
}

/* Hero */
.hero {
  min-height: 465px;
  position: relative;
  background-image: url("https://images.unsplash.com/photo-1580582932707-520aed937b7b?auto=format&fit=crop&w=1900&q=90");
  background-size: cover;
  background-position: center;
  color: #fff;
}

.hero-overlay {
  position: absolute;
  inset: 0;
  background:
    linear-gradient(90deg, rgba(5, 20, 39, 0.82) 0%, rgba(5, 20, 39, 0.65) 42%, rgba(5, 20, 39, 0.1) 80%),
    linear-gradient(0deg, rgba(5, 20, 39, 0.25), transparent);
}

.hero-content {
  min-height: 465px;
  display: flex;
  align-items: center;
  position: relative;
  z-index: 1;
}

.hero-copy {
  max-width: 610px;
  padding: 45px 0;
}

.eyebrow {
  color: var(--orange);
  font-size: 11px;
  font-weight: 800;
  letter-spacing: 1.6px;
  margin-bottom: 12px;
}

.eyebrow.light {
  color: #ffb37f;
}

.hero h1 {
  font-family: Georgia, "Times New Roman", serif;
  font-size: clamp(42px, 5.2vw, 68px);
  line-height: 0.98;
  margin: 0 0 20px;
  letter-spacing: -1.8px;
}

.hero p {
  max-width: 520px;
  font-size: 16px;
  line-height: 1.65;
  color: rgba(255, 255, 255, 0.9);
  margin: 0 0 28px;
}

.hero-actions {
  display: flex;
  flex-wrap: wrap;
  gap: 12px;
}

.btn {
  display: inline-flex;
  justify-content: center;
  align-items: center;
  min-height: 44px;
  border: 0;
  border-radius: 7px;
  padding: 0 20px;
  font-size: 13px;
  font-weight: 750;
  cursor: pointer;
  transition: 0.2s ease;
}

.btn-orange {
  background: var(--orange);
  color: #fff;
}

.btn-orange:hover {
  background: #d95f16;
  transform: translateY(-1px);
}

.btn-outline {
  background: rgba(0, 0, 0, 0.08);
  color: #fff;
  border: 1px solid rgba(255, 255, 255, 0.85);
}

.btn-outline:hover {
  background: #fff;
  color: var(--navy);
}

.play-icon {
  font-size: 10px;
  margin-right: 8px;
}

/* Stats */
.stats-wrap {
  position: relative;
  z-index: 3;
  margin-top: -34px;
}

.stats {
  min-height: 90px;
  background: var(--navy);
  color: #fff;
  border-radius: 8px;
  box-shadow: 0 13px 35px rgba(5, 20, 39, 0.16);
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  overflow: hidden;
}

.stat {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 13px;
  position: relative;
  padding: 18px 15px;
}

.stat:not(:last-child)::after {
  content: "";
  position: absolute;
  right: 0;
  top: 23%;
  bottom: 23%;
  width: 1px;
  background: rgba(255, 255, 255, 0.18);
}

.stat-icon {
  font-size: 27px;
  width: 37px;
  text-align: center;
}

.stat strong,
.stat span {
  display: block;
}

.stat strong {
  font-size: 23px;
  line-height: 1.1;
}

.stat span {
  color: rgba(255, 255, 255, 0.72);
  font-size: 11px;
  margin-top: 4px;
}

/* Highlights */
.highlights {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 17px;
  padding-top: 28px;
  padding-bottom: 55px;
}

.highlight-card {
  text-align: center;
  min-height: 142px;
  border: 1px solid var(--border);
  border-radius: 9px;
  padding: 21px 20px;
  background: #fff;
  box-shadow: 0 4px 15px rgba(15, 30, 45, 0.035);
  transition: 0.2s;
}

.highlight-card:hover {
  transform: translateY(-3px);
  box-shadow: 0 12px 30px rgba(15, 30, 45, 0.09);
}

.highlight-icon {
  font-size: 29px;
  margin-bottom: 8px;
  color: var(--orange);
}

.highlight-card h3 {
  font-family: Georgia, serif;
  font-size: 16px;
  margin: 0 0 7px;
}

.highlight-card p {
  color: var(--muted);
  font-size: 11px;
  line-height: 1.55;
  margin: 0 auto;
  max-width: 190px;
}

/* Sections */
.section {
  padding: 82px 0;
}

.soft-bg {
  background: var(--soft);
}

.section-heading {
  max-width: 660px;
  text-align: center;
  margin: 0 auto 38px;
}

.section-heading h2,
.about-copy h2,
.contact-copy h2 {
  font-family: Georgia, "Times New Roman", serif;
  color: var(--navy-dark);
  font-size: clamp(30px, 3.5vw, 43px);
  line-height: 1.12;
  letter-spacing: -0.8px;
  margin: 0 0 13px;
}

.section-heading p,
.contact-copy > p {
  color: var(--muted);
  line-height: 1.7;
  margin: 0;
  font-size: 14px;
}

/* About */
.about {
  padding-top: 15px;
  padding-bottom: 90px;
}

.about-grid {
  display: grid;
  grid-template-columns: 0.86fr 1.14fr;
  gap: 58px;
  align-items: center;
}

.about-copy h2 {
  font-size: clamp(32px, 3.3vw, 42px);
}

.about-copy > p {
  color: var(--muted);
  font-size: 13px;
  line-height: 1.75;
  max-width: 520px;
}

.about-points {
  display: grid;
  gap: 8px;
  margin: 20px 0 25px;
  font-size: 12px;
  font-weight: 700;
  color: var(--navy);
}

.btn-navy {
  background: var(--navy);
  color: #fff;
}

.btn-navy:hover {
  background: var(--orange);
}

.about-images {
  display: grid;
  grid-template-columns: 1.1fr 0.9fr;
  gap: 14px;
}

.about-main-image {
  height: 360px;
}

.about-side-images {
  display: grid;
  gap: 14px;
}

.about-side-images .image-card {
  height: 173px;
}

.image-card {
  overflow: hidden;
  border-radius: 8px;
}

.image-card img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}

/* Programs */
.programs {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 18px;
}

.program-card {
  background: #fff;
  border: 1px solid var(--border);
  border-radius: 10px;
  padding: 25px;
  display: grid;
  grid-template-columns: 50px 1fr;
  column-gap: 13px;
  position: relative;
  min-height: 175px;
}

.program-number {
  font-family: Georgia, serif;
  color: var(--orange);
  font-size: 26px;
  font-weight: 700;
}

.program-card h3 {
  margin: 2px 0 8px;
  font-family: Georgia, serif;
  color: var(--navy);
  font-size: 19px;
}

.program-card p {
  color: var(--muted);
  font-size: 12px;
  line-height: 1.65;
  margin: 0;
}

.program-card a {
  grid-column: 2;
  color: var(--orange);
  font-size: 12px;
  font-weight: 800;
  margin-top: 18px;
}

/* Campus */
.campus-grid {
  display: grid;
  grid-template-columns: 1.4fr 1fr 1fr;
  grid-auto-rows: 190px;
  gap: 15px;
}

.facility {
  position: relative;
  overflow: hidden;
  border-radius: 9px;
}

.facility:first-child {
  grid-row: span 2;
}

.facility img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.4s;
}

.facility:hover img {
  transform: scale(1.05);
}

.facility-overlay {
  position: absolute;
  inset: auto 0 0;
  padding: 45px 17px 15px;
  color: #fff;
  background: linear-gradient(transparent, rgba(0, 0, 0, 0.7));
}

.facility-overlay span {
  font-weight: 800;
  font-size: 14px;
}

/* Admission */
.admission-banner {
  background: var(--navy);
  color: #fff;
  padding: 62px 0;
}

.admission-inner {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 30px;
}

.admission-inner h2 {
  font-family: Georgia, serif;
  font-size: clamp(29px, 4vw, 44px);
  margin: 0 0 8px;
}

.admission-inner p {
  color: rgba(255,255,255,0.7);
  margin: 0;
  font-size: 14px;
}

/* Gallery */
.gallery-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 13px;
}

.gallery-grid img {
  width: 100%;
  height: 210px;
  object-fit: cover;
  border-radius: 8px;
}

/* Contact */
.contact-grid {
  display: grid;
  grid-template-columns: 1fr 0.85fr;
  gap: 70px;
  align-items: start;
}

.contact-copy h2 {
  margin-bottom: 17px;
}

.contact-details {
  margin-top: 28px;
  display: grid;
  gap: 17px;
}

.contact-details strong,
.contact-details span {
  display: block;
}

.contact-details strong {
  color: var(--navy);
  font-size: 12px;
  margin-bottom: 3px;
}

.contact-details span {
  color: var(--muted);
  font-size: 12px;
}

.enquiry-card {
  background: var(--soft);
  border: 1px solid var(--border);
  border-radius: 10px;
  padding: 28px;
}

.enquiry-card h3 {
  font-family: Georgia, serif;
  color: var(--navy);
  font-size: 25px;
  margin: 0 0 22px;
}

.enquiry-card label {
  display: block;
  color: var(--navy);
  font-size: 11px;
  font-weight: 800;
  margin-bottom: 14px;
}

.enquiry-card input,
.enquiry-card textarea {
  display: block;
  width: 100%;
  margin-top: 6px;
  border: 1px solid #dcdfe4;
  border-radius: 6px;
  padding: 11px 12px;
  background: #fff;
  outline: none;
  resize: vertical;
  color: var(--text);
}

.enquiry-card input:focus,
.enquiry-card textarea:focus {
  border-color: var(--orange);
}

.full {
  width: 100%;
}

.success-message {
  margin-top: 12px;
  padding: 10px;
  border-radius: 6px;
  background: #eaf8ee;
  color: #24753d;
  font-size: 12px;
  text-align: center;
}

/* Footer */
footer {
  background: var(--navy-dark);
  color: #fff;
  padding: 55px 0 20px;
}

.footer-grid {
  display: grid;
  grid-template-columns: 1.5fr 1fr 1fr 1fr;
  gap: 40px;
}

.footer-brand {
  font-weight: 900;
  letter-spacing: 1px;
  font-size: 18px;
}

footer h4 {
  margin: 0 0 15px;
  font-size: 13px;
}

footer a,
footer p {
  display: block;
  color: rgba(255,255,255,0.62);
  font-size: 12px;
  line-height: 1.7;
  margin: 0 0 6px;
}

footer a:hover {
  color: #fff;
}

.muted {
  color: rgba(255,255,255,0.62);
}

.copyright {
  width: min(1160px, calc(100% - 48px));
  margin: 38px auto 0;
  padding-top: 18px;
  border-top: 1px solid rgba(255,255,255,0.1);
  color: rgba(255,255,255,0.42);
  text-align: center;
  font-size: 11px;
}

/* Modal */
.modal-backdrop {
  position: fixed;
  z-index: 100;
  inset: 0;
  display: grid;
  place-items: center;
  padding: 25px;
  background: rgba(4, 12, 25, 0.82);
}

.video-modal {
  width: min(760px, 100%);
  background: #fff;
  border-radius: 12px;
  padding: 12px;
  position: relative;
}

.close-modal {
  position: absolute;
  z-index: 2;
  top: 8px;
  right: 10px;
  border: 0;
  background: rgba(0,0,0,0.55);
  color: #fff;
  width: 32px;
  height: 32px;
  border-radius: 50%;
  font-size: 22px;
  cursor: pointer;
}

.video-placeholder {
  min-height: 400px;
  display: grid;
  place-content: center;
  text-align: center;
  background: #edf1f5;
  border-radius: 8px;
}

.video-placeholder .big-play {
  width: 65px;
  height: 65px;
  display: grid;
  place-items: center;
  margin: 0 auto 15px;
  border-radius: 50%;
  background: var(--orange);
  color: #fff;
}

.video-placeholder h3 {
  font-family: Georgia, serif;
  color: var(--navy);
  margin: 0 0 6px;
}

.video-placeholder p {
  color: var(--muted);
  font-size: 12px;
  margin: 0;
}

/* Responsive */
@media (max-width: 1000px) {
  .nav-links {
    gap: 16px;
  }

  .about-grid {
    gap: 35px;
  }

  .highlights {
    grid-template-columns: repeat(2, 1fr);
  }

  .footer-grid {
    grid-template-columns: 1fr 1fr;
  }
}

@media (max-width: 820px) {
  .topbar-inner {
    justify-content: center;
  }

  .top-links {
    display: none;
  }

  .mobile-menu {
    display: block;
  }

  .nav-links {
    position: absolute;
    display: none;
    left: 0;
    right: 0;
    top: 84px;
    background: #fff;
    padding: 12px 24px 22px;
    box-shadow: 0 12px 20px rgba(0,0,0,0.1);
    flex-direction: column;
    align-items: stretch;
    gap: 0;
  }

  .nav-links.open {
    display: flex;
  }

  .nav-links a,
  .nav-links a:not(.nav-cta)::after {
    padding: 13px 0;
    bottom: auto;
  }

  .nav-links a:not(.nav-cta)::after {
    display: none;
  }

  .nav-cta {
    text-align: center;
    margin-top: 7px;
  }

  .hero,
  .hero-content {
    min-height: 500px;
  }

  .stats {
    grid-template-columns: repeat(2, 1fr);
  }

  .stat:nth-child(2)::after {
    display: none;
  }

  .about-grid,
  .contact-grid {
    grid-template-columns: 1fr;
  }

  .programs {
    grid-template-columns: 1fr;
  }

  .campus-grid {
    grid-template-columns: 1fr 1fr;
    grid-auto-rows: 190px;
  }

  .facility:first-child {
    grid-row: auto;
  }

  .admission-inner {
    flex-direction: column;
    align-items: flex-start;
  }
}

@media (max-width: 560px) {
  .page-container {
    width: min(100% - 30px, 1160px);
  }

  .topbar {
    font-size: 10px;
  }

  .nav-inner {
    min-height: 72px;
  }

  .nav-links {
    top: 72px;
  }

  .brand-logo {
    width: 43px;
    height: 43px;
  }

  .brand-name {
    font-size: 14px;
  }

  .hero,
  .hero-content {
    min-height: 530px;
  }

  .hero h1 {
    font-size: 42px;
  }

  .hero-actions {
    flex-direction: column;
    align-items: stretch;
  }

  .btn {
    width: 100%;
  }

  .stats-wrap {
    margin-top: -20px;
  }

  .stats {
    grid-template-columns: 1fr 1fr;
  }

  .stat {
    justify-content: flex-start;
    padding-left: 18px;
  }

  .stat:nth-child(odd)::after {
    display: block;
  }

  .stat-icon {
    font-size: 21px;
  }

  .stat strong {
    font-size: 19px;
  }

  .highlights {
    grid-template-columns: 1fr;
    padding-top: 22px;
  }

  .about-images {
    grid-template-columns: 1fr;
  }

  .about-main-image {
    height: 250px;
  }

  .about-side-images {
    grid-template-columns: 1fr 1fr;
  }

  .about-side-images .image-card {
    height: 145px;
  }

  .campus-grid,
  .gallery-grid {
    grid-template-columns: 1fr;
  }

  .gallery-grid img {
    height: 220px;
  }

  .footer-grid {
    grid-template-columns: 1fr;
    gap: 28px;
  }

  .copyright {
    width: min(100% - 30px, 1160px);
  }
}
</style>
