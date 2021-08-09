<template>
    <div class="projects">
        <div class="projects__content">
            <h2 class="projects__header">Projects</h2>
        </div>
    </div>
</template>

<script>
export default {
    name: 'Projects',
    props: {
        title: String,
        text: String
    }
}
</script>

<style lang="scss">
    @import '@/assets/scss/_variables.scss';
    .projects {
        background-color: $color-secondary;
        display: block;
    }

    .projects__content {
        padding: 4rem $global-side-padding;
        width: $global-width;
        margin: auto;
    }

    .projects__header {
        font-size: $font-size-md3;
        font-weight: 600;
    }

</style>