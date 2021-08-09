<template>
    <Header />
    <router-view />
    <Footer />
</template>

<script>
    import Header from '@/components/Header.vue'
    import Footer from '@/components/Footer.vue'

    export default {
        name: 'App',
        components: {
            Header,
            Footer
        }
    }
</script>

<style lang="scss">
    @import '@/assets/scss/_variables.scss';
    * {
        box-sizing: border-box;
    }

    body {
        letter-spacing: $letter-spacing-default;
        font-size: $font-size-md;
        font-family: $font-primary;
        font-weight: 400;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;

        background-color: $color-secondary;
        color: $color-black; 

        margin: 0;
        display: block;

        @media screen and (max-width: $mobile-width) {
            font-size: $font-size-sm;
        }
    }

    a {
        color: $color-link;
        text-decoration: underline;

        &:hover {
        color: $color-link-highlight;
        }
    }

    button, .button {
        font-size: $font-size-md;

        background-color: $color-button;
        color: $color-button-text;

        padding: .75rem 1.5rem;
        border: none;
        border-radius: 0.75rem;

        &:hover {
        background-color: $color-button-highlight;
        }
    }

    h1,h2,h3,h4,h5,h6,p{
        margin: 0;
    }
</style>
