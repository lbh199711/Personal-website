<template>
  <div class="gadget__loader lds-ring"><div></div><div></div><div></div><div></div></div>
</template>

<script>
export default {
    name: 'Loader'
}
</script>

<style lang="scss" scoped>
    /*loaded from https://loading.io/css/ */
    @import '@/assets/scss/_variables.scss';

    .lds-ring {
        display: inline-block;
        position: relative;
    }
    .lds-ring div {
        box-sizing: border-box;
        display: block;
        position: absolute;
        width: 80%;
        height: 80%;
        margin: 10%;
        border: 8px solid $color-loader;
        border-radius: 50%;
        animation: lds-ring 1.2s cubic-bezier(0.5, 0, 0.5, 1) infinite;
        border-color: $color-loader transparent transparent transparent;
    }
    .lds-ring div:nth-child(1) {
        animation-delay: -0.45s;
    }
    .lds-ring div:nth-child(2) {
        animation-delay: -0.3s;
    }
    .lds-ring div:nth-child(3) {
        animation-delay: -0.15s;
    }
    @keyframes lds-ring {
        0% {
            transform: rotate(0deg);
        }
        100% {
            transform: rotate(360deg);
        }
    }
</style>