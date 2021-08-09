<template>
    <div class="banner">
        <div class="banner__content">
            <h1 class="banner_title"> {{ title }} </h1>
            <p class="banner_message"> {{ text }} </p>
        </div>
    </div>
</template>

<script>
export default {
    name: 'Banner',
    props: {
        title: String,
        text: String
    }
}
</script>

<style lang="scss">
    @import '@/assets/scss/_variables.scss';
    .banner {
        background-color: $color-secondary;
        display: block;
    }

    .banner__content {
        padding: 4rem $global-side-padding;
        width: $global-width;
        margin: auto;
        text-align: center;
    }

    .banner_title {
        font-size: $font-size-lg;
        font-weight: 600;

        margin-bottom: 1rem;
    }
</style>