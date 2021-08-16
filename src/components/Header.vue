<template>
    <div class="header">
        <div class="header__content">
            <router-link to="/" class="header__link">Leo Liu</router-link>

            <div class="header__links">
                <a href="https://github.com/lbh199711" class="header__link">Github</a>
                |
                <a href="https://www.linkedin.com/in/leo-liu-812984148/" class="header__link">Linkedin</a>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: 'Header'
    }
</script>

<style lang="scss">
    @import '@/assets/scss/_variables.scss';
    .header {
        background-color: $color-primary;
        color: $color-text;

        width: 100%;
    }

    .header__content {
        display: flex;
        justify-content: space-between;
        width: $global-width;
        margin: auto;
        padding: 2rem $global-side-padding 1.75rem;

        @media screen and (max-width: $mobile-width) {
            padding: 2rem $global-side-padding-mobile 1.75rem;
            width: $global-width-mobile;
        }
    }

    .header__link {
        color: $color-text;
        text-decoration: none;

        &:hover {
            color: $color-link-highlight;
        }
    }
</style>
    
