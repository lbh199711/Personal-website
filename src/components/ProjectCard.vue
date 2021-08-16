<template>
    <div class="projectCard">
        <img class="projectCard__img" :src="require('@/assets/imgs/' + imgName + '')" :alt="imgDescription" @click="goToLink"/>
        <div class="projectCard__content">
            <router-link :to="link" class="projectCard__title">{{ title }}</router-link>
            <p class="projectCard__text">{{ text }}</p>
        </div>
    </div>
</template>

<script>
export default {
    name: 'ProjectCard',
    props: {
        title: String,
        imgName: String,
        imgDescription: String,
        text: String,
        link: String
    },
    methods: {
        goToLink: function(e) {
            this.$router.push(this.link);
        }
    }
}
</script>

<style lang="scss">
    @import '@/assets/scss/_variables.scss';
    
    .projectCard {
        display: inline-flex;
        flex-direction: row;
        align-items: flex-start;
        justify-content: flex-start;
        width: 48%;
        margin: 3rem 1% 1rem 1%;

        @media screen and (max-width: $tablet-width) {
            width: 100%;
            margin-right: 0;
        }

        @media screen and (max-width: $mobile-width) {
            margin-top: 2rem;
        }
    }

    .projectCard__img {
        max-width: 250px;
        max-height: 250px;
        width: 30%;
        margin: 0 2rem 0 0;
        cursor: pointer;

        &:hover {
            transform: translateY(-3px) translateX(-1px);
            transition: 100ms;
        }

        @media screen and (max-width: $tablet-width) {
            margin-right: 3rem;
        }

        @media screen and (max-width: $mobile-width) {
            max-width: 150px;
            max-height: 150px;
            margin-right: 1rem;
        }
    }

    .projectCard__title {
        display: block;
        font-size: $font-size-md2;
        font-weight: 600;
        margin-bottom: 1rem;

        @media screen and (max-width: $mobile-width) {
            font-size: $font-size-md;
            margin-bottom: 0;
        }
    }
    
</style>
