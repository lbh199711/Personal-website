<template>
    <div class="experienceCard">
        <h3 class="experienceCard__title">{{ company }}</h3>
        <div class="experienceCard__job" v-for="job in jobs" :key="job.title">
            <p class="experienceCard__jobTitle">{{job.title}}</p>
            <p class="experienceCard__jobTime">{{job.time}}</p>
        </div>
    </div>
</template>

<script>
export default {
    name: 'ExperienceCard',
    props: {
        jobs: Array,
        company: String
    }
}
</script>

<style lang="scss">
    @import '@/assets/scss/_variables.scss';

    .experienceCard {
        margin-top: 3rem;

        @media screen and (max-width: $mobile-width) {
            margin-top: 2rem;
        }
    }

    .experienceCard__title {
        font-size: $font-size-md2;
        font-weight: 400;

        @media screen and (max-width: $mobile-width) {
            font-size: $font-size-md;
        }
    }

    .experienceCard__job {
        margin-top: 1rem;
        @media screen and (max-width: $mobile-width) {
            margin-top: .5rem;
        }
    }
    
    .experienceCard__jobTime {
        color: $color-highlight;
    }
</style>
