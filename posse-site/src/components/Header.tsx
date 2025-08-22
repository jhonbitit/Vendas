import Image from "next/image";
import Link from "next/link";

export default function Header() {
  return (
    <header className="sticky top-0 z-50 w-full border-b border-neutral-200 bg-white/80 backdrop-blur-md dark:border-neutral-800 dark:bg-black/60">
      <div className="mx-auto flex max-w-6xl items-center justify-between px-4 py-3 sm:px-6 lg:px-8">
        <Link href="/" className="flex items-center gap-3">
          <Image src="/logo.svg" alt="Logo" width={36} height={36} priority />
          <span className="text-lg font-semibold tracking-wide">POSSE</span>
        </Link>
        <nav className="hidden items-center gap-6 text-sm font-medium sm:flex">
          <Link href="#sobre" className="text-neutral-600 hover:text-black dark:text-neutral-300 dark:hover:text-white">Sobre</Link>
          <Link href="#instagram" className="text-neutral-600 hover:text-black dark:text-neutral-300 dark:hover:text-white">Instagram</Link>
          <Link href="#facebook" className="text-neutral-600 hover:text-black dark:text-neutral-300 dark:hover:text-white">Facebook</Link>
          <Link href="#contato" className="rounded-full bg-black px-4 py-2 text-white hover:bg-neutral-800 dark:bg-white dark:text-black dark:hover:bg-neutral-200">Contato</Link>
        </nav>
      </div>
    </header>
  );
}