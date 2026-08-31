import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import path from 'path'
import { getProxyOptions } from 'frappe-ui/src/utils/vite-dev-server'
import { webserver_port } from '../../../sites/common_site_config.json'

export default defineConfig({
  base:
    process.env.NODE_ENV === 'production'
      ? '/assets/education_dashboard/frontend/'
      : '/',

  plugins: [vue()],

  server: {
    port: 8081,
    proxy: getProxyOptions({ port: webserver_port }),
  },

  resolve: {
    alias: {
      '@': path.resolve(__dirname, 'src'),
    },
  },

  build: {
    outDir: path.resolve(__dirname, '../education_dashboard/public/frontend'),
    emptyOutDir: true,
    target: 'es2015',
    cssCodeSplit: true,
    minify: 'esbuild',
    sourcemap: false,
  },

  optimizeDeps: {
    include: [
      'frappe-ui > feather-icons',
      'showdown',
      'engine.io-client',
      'debug',
    ],
    esbuildOptions: {
      target: 'esnext',
    },
  },
})