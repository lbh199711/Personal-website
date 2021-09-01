<template>
  <div class="PNF__page">
    <h1 class="PNF__title">404! Page Cannot Be Found!</h1>
    <p class="PNF__scream">OH NOOOOOOO! &#128561;</p>
    <p class="PNF__text">Please double check the url or go back to the <router-link to="/" >homepage</router-link>.</p>
  </div>
</template>

<script>

export default {
  name: 'PageNotFound',
  data () {
    return {
      banner_text: "Welcome to the place where I dump all the cool stuff I have been working on!"
    }
  }
}
</script>

<style lang="scss">
    @import '@/assets/scss/_variables.scss';

    .PNF__page {
        padding: 4rem $global-side-padding 10rem;
        width: $global-width;
        max-width: $global-max-width;
        margin: auto;
        height: 100vh;

        @media screen and (max-width: $mobile-width) {
            padding: 3rem $global-side-padding-mobile 6rem;
            width: $global-width-mobile;
        }
    }

    .PNF__title {
        font-size: $font-size-md3;
        font-weight: 600;
        
        margin-top: 8rem;

        @media screen and (max-width: $mobile-width) {
            font-size: $font-size-md2;
            
            margin-top: 2rem;
        }
    }

    .PNF__scream {
        color: $color-warning;

        margin: 12rem  0 4rem;

        @media screen and (max-width: $mobile-width) {
            margin: 6rem  0 3rem;
        }
    }
</style>
