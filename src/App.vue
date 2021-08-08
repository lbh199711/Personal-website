<template>
  <div id="nav">
    <router-link to="/">Home</router-link> |
    <router-link to="/about">About</router-link>
  </div>
  
  <router-view/>
</template>

<style lang="scss">
@import '@/assets/scss/_variables.scss';

body {
  letter-spacing: $letter-spacing-default;
  font-size: $font-size-md;
  font-family: $font-primary;
  font-weight: 400;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;

  background-color: $color-bg;
  color: $color-black; 

  margin: 0;
  display: block;
}

a {
  color: $color-link;
  text-decoration: underline;

  &:hover {
    color: $color-link-highlight;
  }
}

button, .button {
  font-size: $font-size-md;

  background-color: $color-button;
  color: $color-button-text;

  padding: .75rem 1.5rem;
  border: none;
  border-radius: 0.75rem;

  &:hover {
    background-color: $color-button-highlight;
  }
}

#nav {
  padding: 30px;
  background-color: $color-primary;

  a {
    font-weight: bold;
  }
}
</style>
