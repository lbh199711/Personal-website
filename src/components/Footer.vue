<template>
    <div class="footer">
        <div class="footer__content">
            <p class="footer__text">
                This will be about me, this is a me text.
                Talk about how many line this will have.
                I'm thinking possibly 3 lines of text
            </p>
            <div class="footer__links">
                <a href="https://github.com/lbh199711" class="footer__link">Github</a>
                <a href="https://www.linkedin.com/in/leo-liu-812984148/" class="footer__link">Linkedin</a>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: 'Footer'
    }
</script>

<style lang="scss">
    @import '@/assets/scss/_variables.scss';
    .footer {
        background-color: $color-secondary;
        color: $color-text;
    }

    .footer__content {
        width: $global-width;
        padding: 3.75rem $global-side-padding 4rem;
        justify-content: space-between;
        display: flex;
        margin: auto;

        @media screen and (max-width: $mobile-width) {
            padding: 3.75rem $global-side-padding-mobile 4rem;
            width: $global-width-mobile;
        }
    }

    .footer__text {
        width: 58%;
        margin-right: 2%;
    }

    .footer__link {
        display: block;
        color: $color-text;
        text-decoration: none;

        &:hover {
            color: $color-link-highlight;
        }
    }
</style>
    
