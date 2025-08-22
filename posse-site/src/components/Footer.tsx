export default function Footer() {
  return (
    <footer className="border-t border-neutral-200 bg-white dark:border-neutral-800 dark:bg-black">
      <div className="mx-auto flex max-w-6xl flex-col gap-4 px-4 py-8 text-sm text-neutral-600 dark:text-neutral-400 sm:flex-row sm:items-center sm:justify-between sm:px-6 lg:px-8">
        <p>
          © {new Date().getFullYear()} POSSE. Todos os direitos reservados.
        </p>
        <div className="flex items-center gap-5">
          <a href="#instagram" className="hover:text-black dark:hover:text-white">Instagram</a>
          <a href="#facebook" className="hover:text-black dark:hover:text-white">Facebook</a>
          <a href="#contato" className="hover:text-black dark:hover:text-white">Contato</a>
        </div>
      </div>
    </footer>
  );
}