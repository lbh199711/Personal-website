<template>
    <div class="experience">
        <div class="experience__content">
            <h2 class="experience__header">Professional Experience</h2>
            <ExperienceCard company="Areto Labs" :jobs="[{'title':'Machine Learning Engineer', 'time':'2021.10 - Current'}]" />
            <ExperienceCard company="Dotdash" :jobs="[{'title':'Contractor (Part Time)', 'time':'2020.01 - 2021.04'},{'title':'Software Developer Intern', 'time':'2019.01 - 2019.12'}]" />
            <ExperienceCard company="Hackhub" :jobs="[{'title':'Web Developer Intern', 'time':'2018.09 - 2018.12'}]" />
        </div>
    </div>
</template>

<script>
import ExperienceCard from '@/components/ExperienceCard.vue'
export default {
    name: 'Experience',
    components: {
        ExperienceCard
    }
}
</script>

<style lang="scss">
    @import '@/assets/scss/_variables.scss';
    .experience {
        display: block;
    }

    .experience__content {
        padding: 4rem $global-side-padding 10rem;
        width: $global-width;
        max-width: $global-max-width;
        margin: auto;

        @media screen and (max-width: $mobile-width) {
            padding: 3rem $global-side-padding-mobile 6rem;
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