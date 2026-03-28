<template>
  <div>
    <h2>Contact List</h2>

    <input class="form-control mb-3" v-model="search" placeholder="Search..." />

    <table class="table table-bordered table-striped">
      <thead class="table-dark">
        <tr>
          <th>Name</th>
          <th>Phone</th>
          <th>Email</th>
          <th>Address</th>
        </tr>
      </thead>

      <tbody>
        <tr v-for="c in paginated" :key="c.id">
          <td>{{ c.name }}</td>
          <td>{{ c.phone_number }}</td>
          <td>{{ c.email }}</td>
          <td>{{ c.address }}</td>
        </tr>
      </tbody>
    </table>

    <div class="d-flex justify-content-between">
      <button class="btn btn-primary" @click="prev" :disabled="page === 1">
        Prev
      </button>

      <span>Page {{ page }} / {{ totalPages }}</span>

      <button class="btn btn-primary" @click="next" :disabled="page === totalPages">
        Next
      </button>
    </div>
  </div>
</template>

<script>
import api from "../services/api";

export default {
  data() {
    return {
      contacts: [],
      search: "",
      page: 1,
      size: 5,
    };
  },
  computed: {
    filtered() {
      return this.contacts.filter(
        (c) =>
          c.name.toLowerCase().includes(this.search.toLowerCase()) ||
          c.phone_number.includes(this.search)
      );
    },
    totalPages() {
      return Math.ceil(this.filtered.length / this.size) || 1;
    },
    paginated() {
      const start = (this.page - 1) * this.size;
      return this.filtered.slice(start, start + this.size);
    },
  },
  methods: {
    next() {
      if (this.page < this.totalPages) this.page++;
    },
    prev() {
      if (this.page > 1) this.page--;
    },
  },
  watch: {
    page(val) {
      if (val < 1) this.page = 1;
      if (val > this.totalPages) this.page = this.totalPages;
    },
  },
  async mounted() {
    const res = await api.get("/contacts/");
    this.contacts = res.data;
  },
};
</script>