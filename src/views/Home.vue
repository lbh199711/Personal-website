<template>
  <div class="home">
    <Banner title="&#129409; What is up, my friend &#129409;" :text=banner_text />
    <Projects />
  </div>
</template>

<script>
// @ is an alias to /src
import Banner from '@/components/Banner.vue'
import Projects from '@/components/section/Projects.vue'

export default {
  name: 'Home',
  components: {
    Banner,
    Projects
  },
  data () {
    return {
      banner_text: "First of all, Welcome! Welcome to the place where I dump all the cool stuff I have been working on!"
    }
  }
}
</script>
