<template>
  <div class="home">
    <Banner :title="$route.params.name" :text=project_description />
  </div>
</template>

<script>
// @ is an alias to /src
import Banner from '@/components/Banner.vue'


export default {
  name: 'HomePage',
  components: {
    Banner
  },
  data () {
    return {
      project_description: "First of all, Welcome! Welcome to the place where I dump all the cool stuff I have been working on!"
    }
  }
}
</script>