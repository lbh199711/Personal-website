<template>
    <div class="footer">
        <div class="footer__content">
            <p class="footer__text">
                -> New University of Alberta computer science graduate<br>
                -> Future machine learning engineer<br>
                -> Currently based in Edmonton, Canada
            </p>
            <div class="footer__links">
                <p class="footer__contact">(604) 368-3156</p>
                <p class="footer__contact">lbh199711@gmail.com</p>
                <a href="https://galigio.org/2019/07/08/trained-a-neural-net/" class="footer__button" target="_blank" ><button>Funny Meme</button></a>
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

        max-width: $global-max-width;
        margin: auto;
    }

    .footer__content {
        width: $global-width;
        
        padding: 3.75rem $global-side-padding 4rem;
        display: flex;
        justify-content: space-between;
        margin: auto;

        @media screen and (max-width: $mobile-width) {
            padding: 3.75rem $global-side-padding-mobile 4rem;
            width: $global-width-mobile;
            flex-direction: column;
        }

        @media screen and (min-width: 100rem) {
            width: 100%;
        }
    }

    .footer__text {
        width: 58%;
        margin-right: 2%;

        @media screen and (max-width: $mobile-width) {
            width: $global-width-mobile;
            margin: 0 0 2rem;
        }
    }

    .footer__contact {
        display: block;
        text-decoration: none;
    }

    .footer__button {
        display: block;
        width: max-content;
        margin-top: .5rem;

        @media screen and (max-width: $mobile-width) {
            margin-top: .25rem;
        }
    }
</style>
    
