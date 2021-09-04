<template>
  <div class="home-page">
    <Banner title="What is up, my friend &#129409;" :text=banner_text />
    <Projects />
    <Experience />
  </div>
</template>

<script>
import Banner from '@/components/Banner.vue'
import Projects from '@/components/section/Projects.vue'
import Experience from '@/components/section/Experience.vue'

export default {
  name: 'HomePage',
  components: {
    Banner,
    Projects,
    Experience
  },
  data () {
    return {
      banner_text: "Welcome to the place where I dump all the cool stuff I have been working on!"
    }
  }
}
</script>
