<template>
    <div class="project-page">
        <div v-if="json">
            <Banner :title="json.title" />
            <div class="project-page-content">
                <div class="project-page-content__wrapper">
                    <div class="project-page-content__links">
                        <h3 class="project-page-content__heading">Project Links</h3>
                        <div class="project-page-content__links-wrapper">
                            <a :href="json.url" class="project-page-content__link" target="_blank"><button>Project Repo</button></a>
                            <a :href="json.data" class="project-page-content__link" target="_blank"><button>Input Data</button></a>
                        </div>
                    </div>

                    <template v-for="(object,index) in json.content">
                        <h3 class="project-page-content__heading" v-if="object.type === 'heading'" :key="index+'_heading'">{{object.value}}</h3>
                        <p class="project-page-content__text" v-else-if="object.type === 'text'" :key="index+'_text'">{{object.value}}</p>
                        <p class="project-page-content__text" v-else-if="object.type === 'link'" target="_blank" :key="index+'_link'"><a :href="object.url">{{object.value}}</a></p>
                        <img class="project-page-content__img" v-else-if="object.type === 'image'" :key="index+'_image'" :src="object.value"/>
                    </template>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
// @ is an alias to /src
import Banner from '@/components/Banner.vue'

export default {
    name: 'HomePage',
    components: {
        Banner
    },
    data: function() {
        return {
            json: null
        }
    },
    async created() {
        this.json = await import("@/assets/text/"+this.$route.params.name+".json")
    }
}
</script>

<style lang="scss">
    @import '@/assets/scss/_variables.scss';

    .project-page-content__wrapper {
        padding: 4rem $global-side-padding 10rem;
        width: $global-width;
        max-width: $global-max-width;
        margin: auto;

        @media screen and (max-width: $mobile-width) {
            padding: 3rem $global-side-padding-mobile 6rem;
            width: $global-width-mobile;
        }
    }

    .project-page-content__heading {
        font-size: $font-size-md2;

        margin-top: 3rem;

        &:first-of-type {
            margin-top: 0;
        }

        @media screen and (max-width: $mobile-width) {
            font-size: $font-size-md;
        }
    }

    .project-page-content__text,
    .project-page-content__img {
        margin-top: 2rem;

        @media screen and (max-width: $mobile-width) {
            margin-top: 1rem;
        }
    }

    .project-page-content__img {
        max-width: 100%;
    }

    .project-page-content__links {
        margin-bottom: 3rem;
        display: flex;
        flex-direction: row;
        justify-content: space-between;
        width: 100%;
    }

    .project-page-content__links-wrapper {
        display: flex;
    }

    .project-page-content__link {
        margin-left: 1rem;

        &:first-of-type {
            margin-left: 0;
        }
    }
</style>