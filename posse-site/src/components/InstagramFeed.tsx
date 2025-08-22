"use client";

import { useEffect, useState } from "react";
import Image from "next/image";

type InstagramMedia = {
  id: string;
  media_url: string;
  permalink: string;
};

export default function InstagramFeed() {
  const [items, setItems] = useState<InstagramMedia[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function load() {
      try {
        const res = await fetch("/api/instagram");
        if (!res.ok) throw new Error("Falha ao carregar feed");
        const data = await res.json();
        setItems(data.items || []);
      } catch (e) {
        console.error(e);
      } finally {
        setLoading(false);
      }
    }
    load();
  }, []);

  if (loading) {
    return <div className="text-neutral-500">Carregando…</div>;
  }

  return (
    <div className="grid grid-cols-2 gap-4 sm:grid-cols-3 md:grid-cols-4">
      {items.map((m) => (
        <a key={m.id} href={m.permalink} target="_blank" rel="noreferrer" className="group relative block overflow-hidden rounded-lg">
          <Image src={m.media_url} alt="Instagram media" width={400} height={400} className="h-full w-full object-cover transition-transform group-hover:scale-105" />
        </a>
      ))}
      {items.length === 0 && (
        <div className="col-span-full text-neutral-500">Nenhuma mídia disponível.</div>
      )}
    </div>
  );
}