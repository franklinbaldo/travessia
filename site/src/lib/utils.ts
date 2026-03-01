export function stripMarkdown(md: string | undefined): string {
  return (
    md
      ?.replace(/^#+\s+/gm, "")
      .replace(/[*_~`\[\]()]/g, "")
      .replace(/\n+/g, " ")
      .trim() || ""
  );
}

export function getExcerpt(body: string | undefined, len = 180): string {
  const plain = stripMarkdown(body);
  if (plain.length <= len) return plain;
  return plain.slice(0, len).replace(/\s+\S*$/, "") + "\u2026";
}

export function formatDate(date: Date): string {
  return new Intl.DateTimeFormat("pt-BR", {
    day: "numeric",
    month: "long",
    year: "numeric",
    timeZone: "UTC",
  }).format(date);
}

export function slugToLabel(slug: string): string {
  return slug.replace(/-/g, " ").replace(/_/g, " \u2014 ");
}

export function slugToTitle(slug: string): string {
  return slug.replace(/-/g, " ").replace(/\b\w/g, (c) => c.toUpperCase());
}
