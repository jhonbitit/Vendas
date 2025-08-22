import Image from "next/image";
import { Container } from "@/components/Container";
import InstagramFeed from "@/components/InstagramFeed";
import FacebookEmbed from "@/components/FacebookEmbed";

export default function Home() {
  return (
    <div className="flex min-h-screen flex-col">
      <section className="relative overflow-hidden py-24 sm:py-32">
        <Container>
          <div className="flex flex-col items-center gap-6 text-center">
            <Image src="/logo.svg" alt="POSSE" width={96} height={96} priority />
            <h1 className="text-balance text-4xl font-extrabold tracking-tight sm:text-6xl">
              POSSE
            </h1>
            <p className="max-w-2xl text-balance text-lg text-neutral-600 dark:text-neutral-300">
              Bem-vindo ao site POSSE. Cultura, lifestyle e presença digital.
            </p>
            <div className="mt-4 flex items-center gap-3">
              <a href="#instagram" className="rounded-full bg-black px-6 py-3 text-white hover:bg-neutral-800 dark:bg-white dark:text-black dark:hover:bg-neutral-200">Instagram</a>
              <a href="#facebook" className="rounded-full border border-neutral-300 px-6 py-3 hover:bg-neutral-100 dark:border-neutral-700 dark:hover:bg-neutral-900">Facebook</a>
            </div>
          </div>
        </Container>
      </section>

      <section id="sobre" className="py-16">
        <Container>
          <div className="grid gap-10 md:grid-cols-2 md:items-center">
            <div className="space-y-4">
              <h2 className="text-2xl font-semibold">Sobre</h2>
              <p className="text-neutral-700 dark:text-neutral-300">
                Somos um coletivo criativo. Conteúdo, eventos e collabs com marcas e artistas.
              </p>
            </div>
            <div className="grid grid-cols-3 gap-3">
              <div className="aspect-square rounded-lg bg-neutral-200 dark:bg-neutral-800" />
              <div className="aspect-square rounded-lg bg-neutral-200 dark:bg-neutral-800" />
              <div className="aspect-square rounded-lg bg-neutral-200 dark:bg-neutral-800" />
            </div>
          </div>
        </Container>
      </section>

      <section id="instagram" className="py-16">
        <Container>
          <h2 className="mb-6 text-2xl font-semibold">Instagram</h2>
          <InstagramFeed />
        </Container>
      </section>

      <section id="facebook" className="py-16">
        <Container>
          <h2 className="mb-6 text-2xl font-semibold">Facebook</h2>
          <FacebookEmbed />
        </Container>
      </section>

      <section id="contato" className="py-16">
        <Container>
          <h2 className="mb-6 text-2xl font-semibold">Contato</h2>
          <form className="grid gap-4 sm:max-w-lg">
            <input className="w-full rounded-md border border-neutral-300 bg-transparent px-4 py-3 outline-none placeholder:text-neutral-400 focus:border-black dark:border-neutral-700 dark:focus:border-white" placeholder="Seu nome" />
            <input className="w-full rounded-md border border-neutral-300 bg-transparent px-4 py-3 outline-none placeholder:text-neutral-400 focus:border-black dark:border-neutral-700 dark:focus:border-white" placeholder="Seu email" />
            <textarea className="min-h-32 w-full rounded-md border border-neutral-300 bg-transparent px-4 py-3 outline-none placeholder:text-neutral-400 focus:border-black dark:border-neutral-700 dark:focus:border-white" placeholder="Sua mensagem" />
            <button type="submit" className="rounded-full bg-black px-6 py-3 text-white hover:bg-neutral-800 dark:bg-white dark:text-black dark:hover:bg-neutral-200">Enviar</button>
          </form>
        </Container>
      </section>
    </div>
  );
}
