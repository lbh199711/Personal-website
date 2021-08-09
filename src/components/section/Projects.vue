<template>
    <div class="projects">
        <div class="projects__content">
            <h2 class="projects__header">Projects</h2>
            <ProjectCard imgName="fake-min.jpg" imgDescription="A placeholder image" title="Generate Paintings using DCGAN" text="Some text just to holder place right now and this maybe very long but it doesn't matter as VScode doesn't auto change line." link="/about" />
            <ProjectCard imgName="placeholder.jpg" imgDescription="A placeholder image" title="Currently working on..." text="Leo is not working on anything at the moment. He is either very lazy or occupied in other aspect of life right now..." link="/#" />
        </div>
    </div>
</template>

<script>
import ProjectCard from '@/components/ProjectCard.vue'

export default {
    name: 'Projects',
    components: {
        ProjectCard
    }
}
</script>

<style lang="scss">
    @import '@/assets/scss/_variables.scss';
    .projects {
        background-color: $color-primary;
        display: block;
    }

    .projects__content {
        padding: 3rem $global-side-padding 4rem;
        width: $global-width;
        margin: auto;

        @media screen and (max-width: $mobile-width) {
            padding: 2rem $global-side-padding-mobile 2.5rem;
            width: $global-width-mobile;
        }
    }

    .projects__header {
        font-size: $font-size-md3;
        font-weight: 600;
        
        @media screen and (max-width: $mobile-width) {
            font-size: $font-size-md2;
        }
    }

</style>