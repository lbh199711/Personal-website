<template>
    <div class="sa-model-page">
        <Banner title="Sentiment Analysis Model" />
        <div v-show="!modelStatus" class="loading__wrapper">
            <p class="loading__mesage"> waiting for model to load </p> 
            <Loader class="loading__animation"/>
        </div>
        <div v-show="modelStatus" class="model__wrapper">
            <p class="model__errorMsg" v-show="errorMsg">{{errorMsg}}</p>

            <div v-for="(object,index) in modelStatus" :key="index" class="model__status">
                <h3 class="model__heading">Model Status:</h3>
                <p class="model__text--indent"> Model Version: <span>{{object.version}}</span></p>
                <p class="model__text--indent"> State: <span>"{{object.state}}"</span></p>
                <p class="model__text--indent"> Status: <span>"{{object.status.error_code}}"</span></p>
            </div>

            <div class="model__input-wrapper">
                <h3 class="model__heading">Model Description:</h3>
                <p class="model__text--indent">{{modelDescription}}</p>

                <h3 class="model__heading" v-show="modelOutput != null">Model Output:</h3>
                <p v-show="modelOutput != null" class="model__text--indent model__text--extra-bot-margin">
                    Input Text: <br>
                    &emsp; "{{lastInput}}"
                    </p>
                <p v-show="modelOutput != null" class="model__text--indent">
                    Sentiment Value (0 is negative, 1 is positive):
                    <span :class="'model__output--'+model_sentiment">{{modelOutput}}</span>
                    </p>
                <p v-show="modelOutput != null" class="model__text--indent">
                    Overall, the model thinks the review has a 
                    <span :class="'model__output--'+model_sentiment">{{model_sentiment}}</span>
                    sentiment towards the movie
                </p>

                <h3 class="model__heading">Test out the model here:</h3>
                <textarea v-model="inputString" :placeholder="placeholder" class="model__input" maxlength="8000" minlength="1"></textarea>
                <div class="model__button-wrapper"><button v-on:click="analyze" :disabled="!modelAvailable || inputString===lastInput">Analyze Text</button></div>
            </div>
        </div>

    </div>
</template>

<script>
// @ is an alias to /src
import Banner from '@/components/Banner.vue'
import Loader from '@/components/gadgets/loader.vue'
import { backend_url } from '@/constants.js'
import axios from 'axios'

export default {
    name: 'SaModelPage',
    components: {
        Banner,
        Loader
    },
    data: function() {
        return {
            modelDescription: "This model takes in a movie review and returns a decimal number between 0 and 1, representing the sentiment of the review (Whether the reviewer likes or dislikes the movie). ", 
            modelStatus: null,
            modelOutput: null,
            modelAvailable: false,
            inputString: '',
            lastInput: null,
            placeholder: "Write your review here, or copy from IMDb.",
            errorMsg: ''
        }
    },
    computed: {
        model_sentiment: function () {
            if (this.modelOutput && this.modelOutput > 0.5){
                return 'positive'
            }
            return 'negative'
        }
    },
    methods: {
        analyze: function (e) {
            //validate

            if (typeof this.inputString !=  "string") {
                this.errorMsg = 'Input must be string.'
                this.modelOutput = null
            } else if (this.inputString.length < 1) {
                this.errorMsg = 'The input cannot be empty.'
                this.modelOutput = null
            } else if (this.inputString.length > 8000) {
                this.errorMsg = 'The input exceed maximum character count of 8000.'
                this.modelOutput = null
            } else {
                axios({
                    method: 'post',
                    data:{
                        input_string: this.inputString
                    },
                    url: backend_url+'sentiment-analysis'
                }).then(response => {
                    this.modelOutput = response.data.response.prediction
                    this.lastInput = this.inputString
                    this.inputString = ''
                    this.errorMsg = ''
                })
                .catch(error => {
                    console.log(error)
                    this.errorMsg = error.message
                })
            }
        }
    },
    async mounted () {
        await axios({
            method: 'get',
            url: backend_url+'sentiment-analysis'
        }).then(response => {
            this.modelStatus = response.data.response
            this.modelAvailable = true
        })
        .catch(error => {
            console.log(error)
            this.errorMsg = error.message
            this.modelAvailable = false
            this.modelStatus = [{"version": "null", "state": "null", "status": {"error_code": "connection error", "error_message": "check console log"}}]
        })
    }
}
</script>

<style lang="scss">
    @import '@/assets/scss/_variables.scss';
    .loading__wrapper,
    .model__wrapper {
        padding: 4rem $global-side-padding 10rem;
        width: $global-width;
        max-width: $global-max-width;
        margin: auto;

        @media screen and (max-width: $mobile-width) {
            padding: 3rem $global-side-padding-mobile 6rem;
            width: $global-width-mobile;
        }
    }

    .loading__wrapper {
        color: $color-highlight;
        min-height: 30rem;

        display: flex;
        align-items: center;
        justify-content: center;

        @media screen and (max-width: $mobile-width) {
            min-height: 15rem;
        }
    }

    .loading__animation {
        margin-left: 1rem;
        width: 50px;
        height: 50px;
    }

    .model__errorMsg {
        text-align: center;

        color: $color-warning;

        margin-bottom: 4rem;
    }

    .model__heading {
        font-size: $font-size-md2;

        margin: 4rem 0 1.5rem;
        .model__status & {
            margin-top: 0;
        }

        @media screen and (max-width: $mobile-width) {
            font-size: $font-size-md;

            margin: 3rem 0 1rem;
        }
    }

    .model__text--indent {
        margin: 0.5rem 0 0 2rem;
        @media screen and (max-width: $mobile-width) {
            margin-left: 1rem;
        }
    }

    .model__text--extra-bot-margin {
        margin-bottom: 4rem;
        @media screen and (max-width: $mobile-width) {
            margin-bottom: 3rem;
        }
    }

    .model__input {
        letter-spacing: $letter-spacing-original;
        font-size: $font-size-md;
        font-family: $font-primary;
        font-weight: 400;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;

        width: 100%;
        height: 20rem;

        @media screen and (max-width: $mobile-width) {
            font-size: $font-size-sm;
            letter-spacing: $letter-spacing-default;
            height: 15rem;
        }
    }

    .model__button-wrapper {
        display: flex;
        flex-direction: row;
        justify-content: flex-end;
        align-items: center;
    }

    .model__output--positive {
        font-weight: 600;

        color: $color-highlight;
    }
    .model__output--negative {
        color: $color-warning;
    }
</style>