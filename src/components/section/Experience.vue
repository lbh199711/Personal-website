<template>
    <div class="experience">
        <div class="experience__content">
            <h2 class="experience__header">Professional Experience</h2>
        </div>
    </div>
</template>

<script>

export default {
    name: 'Experience'
}
</script>

<style lang="scss">
    @import '@/assets/scss/_variables.scss';
    .experience {
        background-color: $color-primary;
        display: block;
    }

    .experience__content {
        padding: 3rem $global-side-padding 4rem;
        width: $global-width;
        margin: auto;

        @media screen and (max-width: $mobile-width) {
            padding: 2rem $global-side-padding-mobile 2.5rem;
            width: $global-width-mobile;
        }
    }

    .experience__header {
        font-size: $font-size-md3;
        font-weight: 600;
        
        @media screen and (max-width: $mobile-width) {
            font-size: $font-size-md2;
        }
    }

</style>