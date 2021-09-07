<template>
    <div class="projects">
        <div class="projects__content">
            <h2 class="projects__header">Projects</h2>
            <ProjectCard imgName="sentiment-analysis.png" imgDescription="Logo for IMDb" title="Movie Review Sentiment Analysis" text="Movie review sentiment analysis model created with CNN + LSTM + GloVe Embeddings." link="/project/sentiment-analysis" />
            <ProjectCard imgName="DCGAN.jpg" imgDescription="Image collage made by 9 landscape paintings " title="Generate Paintings Using DCGAN" text="Tensorflow implementation of Deep Convolutional Generative Adversarial Network (DCGAN)" link="/project/DCGAN" />
            <ProjectCard imgName="game-prediction.png" imgDescription="Logo for the game League of Legends" title="League of Legends Game Result Prediction" text="Predicting League of Legends game result using different machine-learning methods" link="/project/game-prediction" />
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
        display: block;
    }

    .projects__content {
        padding: 10rem $global-side-padding 4rem;
        width: $global-width;
        max-width: $global-max-width;
        margin: auto;

        @media screen and (max-width: $mobile-width) {
            padding: 5rem $global-side-padding-mobile 2.5rem;
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