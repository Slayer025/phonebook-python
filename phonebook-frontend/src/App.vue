<template>
  <div>
    <nav class="navbar navbar-dark bg-dark px-3">
      <span class="navbar-brand">Phonebook</span>

      <div>
        <router-link to="/" class="btn btn-light me-2">Home</router-link>
        <router-link to="/create" class="btn btn-success me-2">Add</router-link>
        <router-link to="/manage" class="btn btn-warning">Manage</router-link>
      </div>
    </nav>

    <div class="container mt-4">
      <router-view />
    </div>
  </div>
</template>